import json

from .models import Account

from django.views import View
from django.http import HttpResponse

class SignUpView(View):
  def post(self, request):
    data = json.loads(request.body)
    Account(
      email = data['email'],
      password = data['password']
    ).save()

    return HttpResponse("signup clear", status=200)

class SignInView(View):
  def post(self, request):
    data = json.loads(request.body)

    if Account.objects.filter(email = data['email']).exists():
      user = Account.objects.get(email = data['email'])
      if user.password == data['password']:
        return HttpResponse('login complete!')
      else:
        return HttpResponse("wrong pw!")
    return HttpResponse("what are you doin? Idiot??")

    
