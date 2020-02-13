from .views      import Comments
from django.urls import  path

urlpatterns = [

    path("", Comments.as_view()),
]