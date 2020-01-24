from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length=50)
    postContent = models.CharField(max_length=200)
    postFiles = models.FileField()
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return f"{{self.author}} created post, titled {{self.postTitle}} at {{self.createdDate}}"

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=200)

    def __str__(self):
        return f"{{self.commenter}}\'s comment on post titled {{self.post}}"
