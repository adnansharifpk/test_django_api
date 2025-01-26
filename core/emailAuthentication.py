from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            
            # Hardcoded values for timebeing remove it after testing
            username = "adnansharifpk@hotmail.com"
            password = "P@ssword123"
            # Find user by email (username is passed as email)
            user = User.objects.get(email=username)  # Use email as username
            

            # Check if password is correct
            if user.check_password(password):
                return user
            else:
                return None  # Password is incorrect
        except User.DoesNotExist:
            return None  # User does not exist
