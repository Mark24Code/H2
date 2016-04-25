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
    user_id = str(request.user.id)
    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    c = RequestContext(request, {
        'profile':profile
    })
    return render_to_response('blogs.html',c)

@login_required()
def blogs_api(request):
    if request.GET:
        user_id = request.GET.get('user_id')
        datas = Blog.objects.filter(user_id=user_id).order_by('-created_at')
        items = []
        for data in datas:
            items.append({
                'blog_id':str(data.id),
                'title':data.title,
                'content':data.content,
                'tag':data.tag,
                'created_at':data.created_at.strftime('%Y-%m-%d %H:%M:%S')
                })
        resp = jsonresponse.creat_response(200)
        data = {
            'items':items
        }
        resp.data = data
        return resp.get_response()




@login_required()
def blog(request):
    user_id = str(request.user.id)
    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    if request.GET.get('edit'):
        user_id = request.GET.get('id','')
        blog_id = request.GET.get('blog_id','')
        blog_data = Blog.objects.filter(id=blog_id,user_id=user_id)
        blog = {}
        if blog_data:
            blog_data = blog_data[0]
            blog['title'] = blog_data.title
            blog['content'] = blog_data.content
        c = RequestContext(request, {
            'blog':blog,
            'profile':profile
        })
        return render_to_response('blog.html',c)
    elif request.GET.get('blog_id'):
        user_id = request.GET.get('id','')
        blog_id = request.GET.get('blog_id','')
        blog_data = Blog.objects.filter(id=blog_id,user_id=user_id)
        blog = {}
        if blog_data:
            blog_data = blog_data[0]
            blog['title'] = blog_data.title
            blog['content'] = blog_data.content
        c = RequestContext(request, {
            'blog':blog,
            'frozen':True,
            'profile':profile
        })
        return render_to_response('blog.html',c)

    c = RequestContext(request, {
        'profile':profile
    })
    return render_to_response('blog.html',c)
@login_required()
def blog_api(request):
    if request.POST.get('_method','') == 'put':
        user_id = str(request.user.id)
        blog_title = request.POST.get('blog_title','')
        blog_content = request.POST.get('blog_content','')

        blog = Blog(
            user_id=user_id,
            title=blog_title,
            content=blog_content)
        blog.save()
        blog_id = str(blog.id)

        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/blogs/?id={user_id}'.format(user_id=user_id)
        }
        resp.data = data
        return resp.get_response()

    elif request.POST.get('_method','') == 'post':
        user_id = str(request.user.id)
        blog_id = request.POST.get('blog_id',0)
        blog_title = request.POST.get('blog_title','')
        blog_content = request.POST.get('blog_content','')

        blog = Blog.objects.filter(id=blog_id,user_id=user_id)
        blog.update(
            title=blog_title,
            content=blog_content)
        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/blogs/blog/?id={user_id}&blog_id={blog_id}'.format(user_id=user_id,blog_id=blog_id)
        }
        resp.data = data
        return resp.get_response()