# from django.shortcuts import render

# Create your views here.

import json

from .models import Comment

from django.http import JsonResponse, HttpResponse
from django.views import View

class Comments(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            email = data['email'],
            comment = data['comment']   
        ).save()

        return JsonResponse({'comment':'sssss'})
        
        # JsonResponse({f"{Comment.objects.email}": "saved done!"})

    def get(self, request):
        comment_data = Comment.objects.values()
        # data = json.loads(request.body)
        # comment_data = Comment.objects.get(email = data['email'])


        return JsonResponse({'All the Data':list(comment_data)})
        
        # JsonResponse({'hahaha':list(comment_data)[0].get('comment')})