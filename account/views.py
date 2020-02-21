import json
import bcrypt
import jwt

from .models import Account
from anotherstagram.settings import SECRET_KEY
# import keylike
# SECRET_KEY = keylike.SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse

class SignUpView(View):
  def post(self, request):
    data = json.loads(request.body)

    # print('fdf')
    try:
      if Account.objects.filter(email=data['email']).exists():
        return HttpResponse("already exists!")

      password = data['password'].encode('utf-8')
      passwordsecu = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
      
    
      Account(
        email = data['email'],
        password = passwordsecu
      ).save()

      # print(passwordsecu)

      return HttpResponse("signup clear!")
    
    except KeyError:
      return HttpResponse("reenter plz")

class SignInView(View):
  def post(self, request):
    data = json.loads(request.body)

    if Account.objects.filter(email = data['email']).exists():
      user = Account.objects.get(email = data['email'])

      if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
        access_token = jwt.encode({'email': user.email}, SECRET_KEY).decode('utf-8')
        
        
        return JsonResponse({'access_token':access_token}, status=200)
      
      return HttpResponse(status=401)

    return HttpResponse("what are you doin? signUp first!")
      # if user.password == data['password']:
      #   return HttpResponse('login complete!')
      # else:
      #   return HttpResponse("wrong pw!")

    
