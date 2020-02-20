import jwt

from account import SECRET_KEY
from account.models import Account

from django.http import HttpResponse, JsonResponse