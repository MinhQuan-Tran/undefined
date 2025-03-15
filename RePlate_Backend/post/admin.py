from django.contrib import admin
from .models import Post, Comment, PostImage

class PostImageInline(admin.TabularInline):  # Allows adding images in the Post admin panel
    model = PostImage
    extra = 1  # Allows adding at least one image

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "description", "location", "expire_at", "created_at")
    search_fields = ("description", "location")
    inlines = [PostImageInline]  # Allows images to be managed from the post admin page

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
