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

    c = RequestContext(request, {
        'items':items
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
        blog_id = str(blog.id)

        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/blogs/?id={user_id}&blog_id={blog_id}'.format(user_id=user_id,blog_id=blog_id)
        }
        resp.data = data
        return resp.get_response()

    elif request.POST.get('_method','') == 'post':
        pass
    else:
        # print('>>>>>>>>>>>>>>>>>>>')
        # print(request.url)
        return render_to_response('blog.html',{})

