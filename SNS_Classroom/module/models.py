from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    moduleCode = models.CharField(max_length=10)
    moduleName = models.CharField(max_length=30)
    moduleTeacher = models.ForeignKey(User, on_delete=models.CASCADE)
    studentsEnrolled = models.ManyToManyField(User, blank=True, related_name="student")

    def __str__(self):
        return f"{ self.studentsEnrolled.all() } enrolled for { self.moduleName }"
