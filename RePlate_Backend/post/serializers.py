from rest_framework import serializers
from .models import Comment, PostImage, Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

from rest_framework import serializers
from .models import Comment, PostImage, Post

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["image"]  # Only need the image field

class PostSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Post
        fields = ["title", "description", "location", "quantity", "expire_at", "images"]

    def create(self, validated_data):
        images = validated_data.pop("images", [])  # Extract images

        # Do NOT assign author here, it's assigned in the view
        post = Post.objects.create(**validated_data)

        # Save each image linked to the post
        for image in images:
            PostImage.objects.create(post=post, image=image)

        return post

