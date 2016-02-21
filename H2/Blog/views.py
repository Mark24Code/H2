from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def BlogList(request):
    return HttpResponse("Helloworld")

