from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=50)
    postTitle = models.CharField(max_length=50)
    postContent = models.CharField(max_length=200)
    postFiles = models.FileField()
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{{self.author}} created post, titled {{self.postTitle}} at {{self.createdDate}}"