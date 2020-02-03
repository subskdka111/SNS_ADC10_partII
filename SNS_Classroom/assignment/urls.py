from django.urls import path
from assignment.views import *

urlpatterns = [
    path('', view_assignments),
    path('<int:id>',view_assignment),
    path('create', view_create_assignment),
    path('create/save', create_assignment),
    path('update/<int:id>', view_update_assignment),
    path('update/save/<int:id>', update_assignment),
    path('delete/<int:id>', delete_assignment),
    path('comment/<int:id>', assignment_comment),
    path('uploadfile/<int:id>', upload_file),
    path('deletefile/<int:id>', delete_file),
]
