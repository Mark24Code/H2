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
from django.template import RequestContext

from django.core.urlresolvers import reverse

from core import jsonresponse
from Account.models import UserProfile
from Blog.models import Blog

@login_required()
def blogs(request):
    """
    首页
    """
    print(request.user)
    print(request.user.username)
    print(request.user.id)
    print(request.user.password)
    c = RequestContext(request, {
        "username":request.user.username
        })

    return render_to_response('blogs.html',c)


@login_required()
def blog(request):
    if request.POST.get('_method','') == 'put':
        user_id = str(request.user.id)
        blog_title = request.POST.get('blog_title','')
        blog_content = request.POST.get('blog_content','')
        blog = Blog(
            user_id=user_id,
            title=blog_title,
            content=blog_content)
        blog.save()
        jsonresponse.importtest()
        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/blogs/'
        }
        resp.data = data
        return resp.get_response()

    elif request.POST.get('_method','') == 'post':
        pass
    else:
        return render_to_response('blog.html',{})

