from django.urls import path
from restapi.views import *

urlpatterns = [
    path('', get_review),
    path('<int:id>', get_review_id),
]