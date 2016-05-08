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
from Comment.models import Comment

@login_required()
def comments_api(request):
    if request.GET:
        blog_id = request.GET.get('blog_id',0)
        cur_page = request.GET.get('cur_page',1)
        datas = Comment.objects.filter(blog_id=blog_id).order_by('created_at')
        paged_datas = Paginator(datas,settings.COUNT_PER_PAGE)
        cur_datas = paged_datas.page(cur_page)
        datas = cur_datas.object_list

        pageinfo = {
            "totalPages":int(paged_datas.num_pages),
            "currentPage":int(cur_page)
        }

        items = []
        for data in datas:
            items.append({
                'id':str(data.id),
                'blog_id':data.blog_id,
                'nickname':data.nickname,
                'mail':data.mail,
                'created_at':data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        resp = jsonresponse.creat_response(200)
        data = {
            'comment_list':items,
            'pageinfo':pageinfo
        }
        resp.data = data
        return resp.get_response()

@login_required()
def comment_api(request):

    if request.POST.get('_method','') == 'put':
        blog_id = request.POST.get('blog_id','')
        comment_nickname = request.POST.get('comment_nickname','')
        comment_email = request.POST.get('comment_email','')
        comment_content = request.POST.get('comment_content','')

        comment = Comment(
            blog_id=blog_id,
            nickname=comment_nickname,
            content=comment_content)
        comment.save()
        comment_id = str(comment.id)

        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/blogs/blog/?blog_id={blog_id}'.format(blog_id=blog_id)
        }
        resp.data = data
        return resp.get_response()
