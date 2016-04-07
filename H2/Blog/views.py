from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


def Blog(request):
    return render_to_response('blog.html',{})

def BlogList(request):
    return render_to_response('bloglist.html',{})

def BlogEdit(request):
    return render_to_response('blogedit.html',{})

