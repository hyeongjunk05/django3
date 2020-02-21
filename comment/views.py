# from django.shortcuts import render

# Create your views here.

import json

from .models import Comment
from auth.utils import login_request

from django.http import JsonResponse, HttpResponse
from django.views import View


class Comments(View):
    # print('ddd1')
    @login_request
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            email = request.agent.email,#data['email'],
            comment = data['comment']   
        ).save()
        # print('dfd')

        return HttpResponse(status=200)
        
        # JsonResponse({f"{Comment.objects.email}": "saved done!"})

    @login_request
    def get(self, request):
        comment_data = Comment.objects.values()
        # data = json.loads(request.body)
        # comment_data = Comment.objects.get(email = data['email'])


        return JsonResponse({'All the Data':list(comment_data)},status=200)
        
        # JsonResponse({'hahaha':list(comment_data)[0].get('comment')})