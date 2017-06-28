# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        return HttpResponse("Response to GET Request!")
    elif request.method == 'POST':
        user_name = request.POST['name']
        user_id = request.POST['id']
        return HttpResponse("Hello, This is the mobile app!" + user_name + ' ' + user_id)
        # return HttpResponse("Response to POST Request!")
    return HttpResponse("Other Http Request Method")