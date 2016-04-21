import json
import traceback
from django.contrib import auth
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

from django.http import Http404
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from core import jsonresponse
from Account.models import UserProfile

@login_required()
def blogs(request):
    """
    首页
    """
    return render_to_response('index.html',{})


@login_required()
def blog(request):
    return render_to_response('blog.html',{})

