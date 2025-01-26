from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status  # Importing the status module

# Authentication Views
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user using the email and password
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If user is authenticated, create a JWT token
            token = RefreshToken.for_user(user)
            return Response({'access': str(token.access_token), 'refresh': str(token)}
                            )
        else:
            return Response({"detail": "Invalid credentials"}, status=401)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Retrieve the refresh token from the request
        refresh_token = request.data.get('refresh')

        if refresh_token is None:
            return Response({"detail": "Refresh token is required for logout."}, status=400)

        try:
            # Will implement in future Blacklist the refresh token
            #token = RefreshToken(refresh_token)
            #token.blacklist()

            return Response({"detail": "Logged out successfully."}, status=200)

        except Exception as e:
            # Handle any errors during the token invalidation process
            return Response({"detail": "Invalid refresh token."}, status=400)


# Porduct Views

class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get('name', '')  # Using 'name' for search filtering
        order_by = request.GET.get('order_by', 'name')  # Default order by 'name'
        sort_direction = request.GET.get('sort_direction', 'asc')  # Default sort direction is 'asc'
        
        # Validate the ordering field to ensure it's a valid field in the model
        valid_order_fields = ['id', 'stock', 'name', 'description', 'price', 'selected']  # Add fields you want to allow for ordering
        if order_by not in valid_order_fields:
            raise ValidationError(f"Invalid order_by field. Valid fields are: {', '.join(valid_order_fields)}")
        
        # Validate sort direction
        if sort_direction not in ['asc', 'desc']:
            raise ValidationError("Invalid sort_direction. Must be either 'asc' or 'desc'.")
        
        # Apply search filter and sorting
        if query:
            products = Product.objects.filter(name__icontains=query).order_by(order_by if sort_direction == 'asc' else f'-{order_by}')
        else:
            products = Product.objects.all().order_by(order_by if sort_direction == 'asc' else f'-{order_by}')
        
        # Serialize and return data
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class UpdateProductSelectionView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, product_id):
        try:
            # Fetch the product by its ID
            product = Product.objects.get(id=product_id)

            # Retrieve the 'selected' status from the request data (default to the current value if not provided)
            selected = request.data.get('selected', None)
            
            if selected is not None:
                # Update the 'selected' field with the new value
                product.selected = selected
                product.save()

                # Serialize the updated product
                serializer = ProductSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "'selected' field is required."}, status=status.HTTP_400_BAD_REQUEST)

        except Product.DoesNotExist:
            # Return a 404 if the product does not exist
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Catch any other errors
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)