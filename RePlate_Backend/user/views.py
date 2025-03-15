from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.conf import settings
import os

User = get_user_model()

@api_view(['POST'])
def google_auth(request):
    token = request.data.get("token")
    if not token:
        return Response({"error": "Token is required"}, status=400)

    try:
        # Verify Google token
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.getenv("GOOGLE_CLIENT_ID"))

        # Extract user info
        email = idinfo["email"]
        name = idinfo.get("name", "")
        picture = idinfo.get("picture", "")

        # Create or update user
        user, created = User.objects.get_or_create(username=email, defaults={
            "email": email,
            "first_name": name
        })

        if created:
            user.user_type = "individual"  # Default user type
            user.profile_picture = picture  # Only if the model has this field
            user.rating = 0  # Default rating
            user.save()

        # Generate authentication token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "email": user.email,
            "name": user.first_name,
            "profile_picture": picture,
            "user_type": getattr(user, "user_type", "user"),
            "rating": getattr(user, "rating", 0)
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["GET"])
def get_user_data(request):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return Response({"error": "Token not provided"}, status=401)

    token_key = auth_header.split(" ")[1]
    try:
        token = Token.objects.get(key=token_key)
        user = token.user  # Get user linked to token
        return Response({
            "name": user.get_full_name() or user.username,
            "email": user.email,
            "profile_picture": user.profile_picture if isinstance(user.profile_picture, str) else None,
            "user_type": getattr(user, "user_type", "user"),
            "rating": getattr(user, "rating", 0)
        })
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)
