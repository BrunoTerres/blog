from django.urls import path
from post.views import all, get_one, save

urlpatterns = [
    path('/', all),
    path('/<int:id>', get_one),
    path('/save', save),
]
