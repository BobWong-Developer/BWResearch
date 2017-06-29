# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    if request.method == 'GET':
        return HttpResponse("Response to GET Request!")
    elif request.method == 'POST':
        return HttpResponse("Response to POST Request!")

        # form type
        # user_name = request.POST['name']
        # user_id = request.POST['id']
        # return HttpResponse("Hello, This is the mobile app!" + user_name + ' ' + user_id)

        # request_body = request.body
        # request_body = request.body.decode('utf-8')
        #
        # json_object = json.loads(request_body)
        # user_name = json_object['a']
        # # user_name = json_object.a
        # response_string = 'POST response: ' + user_name
        #
        # return HttpResponse(response_string)
        #
        # response_json_dict = {'a': 'abc', 'b': 'bcd', 'c': 'cde'}
        # response_json_string = json.dumps(response_json_dict)
        # return HttpResponse(response_json_string)

    return HttpResponse("Other Http Request Method")

def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        return HttpResponse("Number is " + username)
        # return HttpResponse("Login Successfully GET!")
    elif request.method == 'POST':
        return HttpResponse("Login Successfully POST!")