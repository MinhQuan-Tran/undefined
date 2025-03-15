from rest_framework import serializers
from .models import Comment, PostImage, Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["image"]  # Only need the image field

class PostSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False  # Accept multiple image uploads
    )

    class Meta:
        model = Post
        fields = ["description", "location", "quantity", "expiration_day", "images"]  # Only user-defined fields

    def create(self, validated_data):
        images = validated_data.pop("images", [])  # Extract images before saving
        post = Post.objects.create(author=self.context["request"].user, **validated_data)

        # Save each image linked to the post
        for image in images:
            PostImage.objects.create(post=post, image=image)

        return post
