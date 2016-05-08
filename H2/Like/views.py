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
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.conf import settings
from core import jsonresponse
from Account.models import UserProfile
from Like.models import Like
from Comment.models import Comment


@login_required()
def like_api(request):
    # if request.POST.get('_method','') == 'put':
    #     user_id = str(request.user.id)
    #     like_title = request.POST.get('like_title','')
    #     like_content = request.POST.get('like_content','')

    #     like = Like(
    #         user_id=user_id,
    #         title=like_title,
    #         content=like_content)
    #     like.save()
    #     like_id = str(like.id)

    #     resp = jsonresponse.creat_response(200)
    #     data = {
    #         'url':'/likes/?id={user_id}'.format(user_id=user_id)
    #     }
    #     resp.data = data
    #     return resp.get_response()

    # elif request.POST.get('_method','') == 'delete':
    #     user_id = str(request.user.id)
    #     like_id = request.POST.get('like_id',0)
    #     like_title = request.POST.get('like_title','')
    #     like_content = request.POST.get('like_content','')

    #     like = Like.objects.filter(id=like_id,user_id=user_id)
    #     like.update(
    #         title=like_title,
    #         content=like_content)
    #     resp = jsonresponse.creat_response(200)
    #     data = {
    #         'url':'/likes/like/?id={user_id}&like_id={like_id}'.format(user_id=user_id,like_id=like_id)
    #     }
    #     resp.data = data
    #     return resp.get_response()
    # elif request.GET:
    print('>>>FFF')

    user_id = str(request.user.id)
    blog_id = request.GET.get('blog_id','')
    try:
        like_data = Like.objects.filter(blog_id=blog_id).order_by('id')
        like = len(like_data)
    except:
        like = 0
    print(like)

    resp = jsonresponse.creat_response(200)
    data = {
        'like':like
    }
    resp.data = data
    return resp.get_response()