from django.urls import path
from module.views import *

urlpatterns = [
    path('', view_modules),
]