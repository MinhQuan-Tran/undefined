from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

User = get_user_model()

# --- POST VIEWS ---

@api_view(['GET'])
def list_posts(request):
    """Get all posts"""
    posts = Post.objects.all()
    post_list = []

    for post in posts:
        post_data = {
            "id": post.id,  # Post ID
            "author": post.author.username,  # Author's Username
            "title": post.title,
            "description": post.description,
            "location": post.location,
            "quantity": post.quantity,
            "expire_at": post.expire_at,
            "created_at": post.created_at,
            "image_urls": [image.image.url for image in post.images.all()]  # List of Image URLs
        }
        post_list.append(post_data)

    return Response(post_list)

@api_view(['GET'])
def get_post(request, post_id):
    """Retrieve a single post"""
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])  # Enable file uploads
def create_post(request):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return Response({"error": "Token not provided"}, status=401)

    token_key = auth_header.split(" ")[1]
    try:
        token = Token.objects.get(key=token_key)
        user = User.objects.filter(id=token.user.id).first()  # Fetch the authenticated user

        if not user:
            return Response({"error": "User not found"}, status=404)

        # Pass the user to the serializer
        serializer = PostSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            post = serializer.save(author=user)  # Ensure author is assigned correctly
            return Response(
                {"message": "Post created successfully!", "post_id": post.id},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)




@api_view(['DELETE'])
def delete_post(request, post_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return Response({"error": "Token not provided"}, status=401)

    token_key = auth_header.split(" ")[1]
    try:
        token = Token.objects.get(key=token_key)
        user = User.objects.filter(id=token.user.id).first()

        if not user:
            return Response({"error": "User not found"}, status=404)

        """Delete a post (only the author can delete)"""
        post = get_object_or_404(Post, id=post_id, author=user)

        if post.author != request.user:
            return Response({"error": "You do not have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)


# --- COMMENT VIEWS ---

@api_view(['GET'])
def list_comments(request, post_id):
    """List all comments for a post"""
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(parent__isnull=True)  # Get only top-level comments
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, post_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return Response({"error": "Token not provided"}, status=401)

    token_key = auth_header.split(" ")[1]
    try:
        token = Token.objects.get(key=token_key)
        user = User.objects.filter(id=token.user.id).first()

        if not user:
            return Response({"error": "User not found"}, status=404)

        """Create a comment for a post"""
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data, context={
            'request': request,
            'author': user
        })
        if serializer.is_valid():
            serializer.save(author=user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)

@api_view(['POST'])
def reply_to_comment(request, post_id, comment_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return Response({"error": "Token not provided"}, status=401)

    token_key = auth_header.split(" ")[1]
    try:
        token = Token.objects.get(key=token_key)
        user = User.objects.filter(id=token.user.id).first()

        if not user:
            return Response({"error": "User not found"}, status=404)

        """Reply to a comment"""
        post = get_object_or_404(Post, id=post_id)
        parent_comment = get_object_or_404(Comment, id=comment_id, post=post)

        serializer = CommentSerializer(data=request.data, context={
            'request': request, 
            'author': user
        })
        if serializer.is_valid():
            serializer.save(author=user, post=post, parent=parent_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)

@api_view(['DELETE'])
def delete_comment(request, post_id, comment_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return Response({"error": "Token not provided"}, status=401)

    token_key = auth_header.split(" ")[1]
    try:
        token = Token.objects.get(key=token_key)
        user = User.objects.filter(id=token.user.id).first()

        if not user:
            return Response({"error": "User not found"}, status=404)

        """Delete a comment (only author can delete, also deletes replies)"""
        comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)

        if comment.author != request.user:
            return Response({"error": "You do not have permission to delete this comment."}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()  # Django cascades deletion to all replies
        return Response({"message": "Comment and its replies deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)
