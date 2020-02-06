from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
            return f"{self.name} - {self.email}"
