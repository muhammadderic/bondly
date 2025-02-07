from django.urls import path
from .views import home, add_post, update_post, delete_post

urlpatterns = [
  path('', home, name='home'),
  path('add', add_post, name='add_post'),
  path('update/<int:post_id>', update_post, name='update_post'),
  path('delete/<int:post_id>', delete_post, name='delete_post'),
]