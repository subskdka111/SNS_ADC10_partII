from restapi.models import Review
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_review(request):
    if request.method == "GET":
        reviews = Review.objects.all().values("name", "email", "content")
        review_objects = list(reviews)
        dict_obj = {
            "reviews" : review_objects
        }
        return JsonResponse(dict_obj)

@csrf_exempt
def get_review_id(request, id):
    review = Review.objects.get(id=id)
    if request.method == "GET":
        return JsonResponse({
            "name" : review.name,
            "email" : review.email,
            "content" : review.content
        })
