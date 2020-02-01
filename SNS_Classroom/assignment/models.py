from django.db import models
from django.contrib.auth.models import User
from module.models import Module

class Assignment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignmentTitle = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    assignmentQuestionPapers = models.FileField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-createdDate"]

    def __str__(self):
        return f"{self.assignmentTitle} assigned at {self.createdDate} by {self.author}"

    def postedBy(self):
        return self.author

    def getModule(self):
        return self.module

class AssignmentComment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.commenter}\'s comment on Assignment titled {self.assignment.assignmentTitle}"

class StudentsFile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Studentsfile = models.FileField()

    def __str__(self):
        return f"{ self.student }\'s assignment file for { self.assignment.assignmentTitle }"

    def getAssignment(self):
        return self.assignment
