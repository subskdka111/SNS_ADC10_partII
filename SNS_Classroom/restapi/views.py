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
    elif request.method == "POST":
        dictionary_objects = json.loads(request.body)
        Review.objects.create(name=dictionary_objects['name'], email=dictionary_objects['email'], content=dictionary_objects['content'])
        return JsonResponse({
            "message": "Posted Successfully"
        })
    else:
        return HttpResponse("Other Requests not Found")

@csrf_exempt
def get_review_id(request, id):
    review = Review.objects.get(id=id)
    if request.method == "GET":
        return JsonResponse({
            "name" : review.name,
            "email" : review.email,
            "content" : review.content
        })
    elif request.method == "PUT":
        dictionary_objects = json.loads(request.body)
        review.name=dictionary_objects['name']
        review.email=dictionary_objects['email']
        review.content=dictionary_objects['content']
        review.save()
        return JsonResponse({
            "message" : "Post Updated Successfully"
        })
    else:
        return HttpResponse("Other Requests not Found")
