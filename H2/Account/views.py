from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html',{})

def login(request):
    return render_to_response('login.html',{})