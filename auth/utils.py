import jwt
# import json

from account.models import Account
from anotherstagram.settings import SECRET_KEY
# import keylike
# SECRET_KEY = keylike.SECRET_KEY

# SECRET_KEY = keylike.SECRET_KEY

from django.http import HttpResponse, JsonResponse



def login_request(func):
    
    def wrapper(self, request, *args, **kwargs):
        
        access_token = request.headers.get('Authorization', None)
        token_decoded = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')['email']
        agent = Account.objects.get(email = token_decoded)
        request.agent =  agent
        print('good2')
        
        
    
        return func(self, request, *args, **kwargs)
    return wrapper