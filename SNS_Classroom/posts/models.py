from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length=50)
    postContent = models.CharField(max_length=200)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.author} created post, titled {self.postTitle} at {self.createdDate}"

    def postedBy(self):
        return self.author

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.commenter}\'s comment on post titled {self.post}"
    
    def commentFrom(self):
        return self.post

class PostFiles(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField()
    originalFileName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.file} from post {self.post}"