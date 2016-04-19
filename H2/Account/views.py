from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

# def index(request):
#     print(111111111111111);
#     return render_to_response('index.html',{})
def index(request):
    print(111111111111111);
    return render_to_response('login.html',{})

# def login(request):
#     return render_to_response('login.html',{})