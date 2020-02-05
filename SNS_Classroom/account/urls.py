from django.urls import path
from .views import *

urlpatterns = [
    path('login', view_login),
    path('signup', view_signup),
    path('profile/<int:id>', view_profile),
    path('logout', view_logout),
]