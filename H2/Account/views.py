from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse('index6666')