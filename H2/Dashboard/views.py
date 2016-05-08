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
def stat(request):
    """仪表盘"""
    user_id = str(request.user.id)

    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    c = RequestContext(request, {
        'siderbar':True,
        'siderbar_name':'sider_stat',
    })

    return render_to_response('dashboard_stat.html',c)

def comments(request):
    """评论"""

    c = RequestContext(request, {
        'siderbar':True,
        'siderbar_name':'sider_comments',
    })

    return render_to_response('dashboard_comments.html',c)

def blogs(request):
    """博客管理"""

    c = RequestContext(request, {
        'siderbar':True,
        'siderbar_name':'sider_blogs',
    })

    return render_to_response('dashboard_blogs.html',c)

def trash(request):
    """垃圾桶"""

    c = RequestContext(request, {
        'siderbar':True,
        'siderbar_name':'sider_trash',
    })

    return render_to_response('dashboard_trash.html',c)

def filter(request):
    """过滤器"""

    c = RequestContext(request, {
        'siderbar':True,
        'siderbar_name':'sider_filter',
    })

    return render_to_response('dashboard_filter.html',c)