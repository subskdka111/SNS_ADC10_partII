from django.contrib import admin
from .models import Assignment, AssignmentComment, StudentsFile

admin.site.register(Assignment)
admin.site.register(AssignmentComment)
admin.site.register(StudentsFile)
