import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.http import HttpResponse

from post.helper import Conversor
from post.models import Post
from user.models import User


def all(request) -> HttpResponse:
    posts = Post.objects.all()
    return JsonResponse(Conversor.models_dict(posts), safe=False)


def get_one(request, id: int) -> HttpResponse:
    try:
        post = Post.objects.get(pk=id)
        return JsonResponse(Conversor.model_dict(post), safe=False)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)


def save(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    post_date = json.loads(request.body)
    user = User.objects.get(pk=1)

    print(user)
    Post.objects.create(author=user, **post_date)
