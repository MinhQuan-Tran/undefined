from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.conf import settings
import os

User = get_user_model()  # Use the correct user model

@api_view(['POST'])
def google_auth(request):
    token = request.data.get("token")
    try:
        # Verify token with Google
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.environ.get("GOOGLE_CLIENT_ID"))

        # Extract user info
        email = idinfo["email"]
        name = idinfo.get("name", "")
        picture = idinfo.get("picture", "")  # Get profile picture

        # Create or update user
        user, created = User.objects.get_or_create(username=email, defaults={"email": email, "first_name": name})
        if created:
            user.user_type = "individual"  # Set default user type
            user.profile_picture = picture  # If you have a profile picture field
            user.rating = null  # Set default rating
            user.save()

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "email": user.email, "name": user.first_name, "profile_picture": picture, "user_type": user.user_type, "rating": user.rating})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
