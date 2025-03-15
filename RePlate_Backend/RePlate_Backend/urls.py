"""
URL configuration for RePlate_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.views import google_auth
from post.views import list_posts, create_post, get_post, delete_post, list_comments, create_comment, reply_to_comment, delete_comment

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/google/', google_auth, name="google_auth"),

    path('posts/', list_posts, name='list_posts'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/', get_post, name='get_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),

    path('posts/<int:post_id>/comments/', list_comments, name='list_comments'),
    path('posts/<int:post_id>/comments/create/', create_comment, name='create_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/reply/', reply_to_comment, name='reply_to_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
