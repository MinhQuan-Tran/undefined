from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import os

@api_view(['POST'])
def google_auth(request):
    token = request.data.get("token")
    try:
        # Verify token with Google
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.getenv("GOOGLE_CLIENT_ID"))

        # Extract user info
        email = idinfo["email"]
        name = idinfo.get("name", "")
        
        user, created = User.objects.get_or_create(username=email, defaults={"email": email, "first_name": name})
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "email": user.email})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
