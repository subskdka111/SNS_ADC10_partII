from django.urls import path
from module.views import *

urlpatterns = [
    path('', view_modules),
    path('enroll/<int:id>', add_student_in_module),
    path('<int:id>', view_all_post_of_certain_module),
]
