from django.db import models

class Post(models.Model):
  post_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
