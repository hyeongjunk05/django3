from django.urls import path
from .views      import SignUpView, SignInView

urlpatterns = [
    # path('', SignUpView.as_view()),
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
]