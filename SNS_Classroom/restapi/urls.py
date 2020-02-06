from django.urls import path
from restapi.views import *

urlpatterns = [
    path('', get_review),
    path('<int:id>', get_review_id),
    path('<int:pageno>/<int:size>', get_review_by_pagination),
]