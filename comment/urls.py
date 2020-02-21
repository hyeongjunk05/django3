from .views      import Comments
from django.urls import  path

urlpatterns = [

    path("/com", Comments.as_view()),
]