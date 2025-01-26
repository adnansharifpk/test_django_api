# api/authGuard.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class AuthGuard:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip authentication check on the /login route
        if request.path == '/api/login/':
            return self.get_response(request)

        # Check for Authorization header
        auth = request.headers.get('Authorization', None)

        if auth is None:
            raise AuthenticationFailed("Authorization token not provided")

        try:
            # Attempt to authenticate the token using the JWTAuthentication class
            jwt_auth = JWTAuthentication()
            user, auth_token = jwt_auth.authenticate(request)
            request.user = user  # Set the authenticated user
        except AuthenticationFailed as e:
            raise e

        response = self.get_response(request)
        return response
