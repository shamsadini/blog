from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    video = models.FileField(upload_to='article_videos/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def increment_views(self):
        self.views += 1
        self.save()
    
