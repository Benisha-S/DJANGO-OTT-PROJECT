from django.contrib.auth.hashers import check_password
from .models import UserProfile

def authenticate_customer(email, password):
    try:
        user = UserProfile.objects.get(email=email)
        if check_password(password, user.password):
            return user
    except UserProfile.DoesNotExist:
        return None
