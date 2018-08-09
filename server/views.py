# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

done = False

@csrf_exempt
def restaurant1(request):
    if request.method == "POST":
        request_data = json.loads(request.body.decode('utf-8'))
        request_data['id'] = 1
        response_data = {
            'status': 'success',
            'data': request_data
        }
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=201)


@csrf_exempt
def restaurant2(request, id):
    global done
    if request.method == "GET":
        if done is False:
            request_data = {"id": 1, "name": "Flying Spaghetti Monster", "cuisines": ["italian", "continental"], "city": "Wadiya", "latitude": 8.121212, "longitude": 5.35239, "rating": 8.1, "is_open": True}

            response_data = {
                'status': 'success',
                'data': request_data
            }
            done = True
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
        else:
            return HttpResponse(status=404)
    elif request.method == "DELETE":
        return HttpResponse(status=200)

