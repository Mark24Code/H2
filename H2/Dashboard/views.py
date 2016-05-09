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
from datetime import datetime,date, timedelta
from collections import OrderedDict

from core import jsonresponse
from Account.models import UserProfile
from Blog.models import Blog
from Comment.models import Comment
from Like.models import Like

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
        'profile':profile,
        'siderbar':True,
        'siderbar_name':'sider_stat',
    })

    return render_to_response('dashboard_stat.html',c)

@login_required()
def stat_api(request):
    """仪表盘数据"""
    user_id = str(request.user.id)

    delta = 30
    today = date.today()+timedelta(days=1)#.strftime('%Y-%m-%d %H:%M:%S')
    month_ago = (date.today()-timedelta(days=delta))#.strftime('%Y-%m-%d %H:%M:%S')
    order = [i for i in range(delta-1,-1,-1)]
    date_list = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in order]

    #blog stat
    blog_datas = Blog.objects.filter(user_id=user_id,created_at__gt=month_ago,created_at__lte=today).order_by("-created_at")
    blog_ids = [str(blog.id) for blog in blog_datas]


    blog_date_list = [blog.created_at.strftime('%Y-%m-%d') for blog in blog_datas]
    date2blog_id_list = OrderedDict()
    for blog in blog_datas:
        blog_created_at = blog.created_at.strftime('%Y-%m-%d')
        if blog_created_at in date2blog_id_list:
            date2blog_id_list[blog_created_at].append(str(blog.id))
        else:
            date2blog_id_list[blog_created_at] = [str(blog.id)]

    blog_count_list = []
    for date_txt in date_list:
        blog_count = blog_date_list.count(date_txt)
        blog_count_list.append(blog_count)

    # print("[",len(blog_count_list),"]blog_count_list:",blog_count_list)
    #comment stat
    comment_datas = Comment.objects.filter(blog_id__in=blog_ids)
    blog_id2comment = {}
    for comment in comment_datas:
        blog_id = comment.blog_id
        if blog_id in blog_id2comment:
            blog_id2comment[blog_id].append(comment)
        else:
            blog_id2comment[blog_id] = [comment]

    date2comment_count = {}
    for one_date in date2blog_id_list:
        blog_id_list = date2blog_id_list[one_date]
        one_date_comment_count = 0
        for blog_id in blog_id_list:
            one_date_comment_count += len(blog_id2comment[blog_id])  if blog_id2comment.get(blog_id,[]) else 0
        date2comment_count[one_date] = one_date_comment_count

    comment_count_list = []
    for date_txt in date_list:
        if date_txt in date2comment_count:
            comment_count_list.append(date2comment_count[date_txt])
        else:
            comment_count_list.append(0)

    # print("[",len(comment_count_list),"]comment_count_list:",comment_count_list)
    #like stat
    like_datas = Like.objects.filter(blog_id__in = blog_ids)
    blog_id2like = {}

    for like in like_datas:
        blog_id = like.blog_id
        if blog_id in blog_id2like:
            blog_id2like[blog_id].append(like)
        else:
            blog_id2like[blog_id] = [like]
    date2like_count = {}
    try:
        for one_date in date2blog_id_list:
            blog_id_list = date2blog_id_list[one_date]
            one_date_like_count = 0
            for blog_id in blog_id_list:
                one_date_like_count += len(blog_id2like[blog_id]) if blog_id2like.get(blog_id,[]) else 0
            date2like_count[one_date] = one_date_like_count
    except:
        traceback.print_exc()
    like_count_list = []
    for date_txt in date_list:
        if date_txt in date2like_count:
            like_count_list.append(date2like_count[date_txt])
        else:
            like_count_list.append(0)
    # print("[",len(like_count_list),"]like_count_list:",like_count_list)


    data = {
        'blog_count_list':blog_count_list,
        'comment_count_list':comment_count_list,
        'like_count_list':like_count_list,
        'date_list':date_list
    }
    resp = jsonresponse.creat_response(200)
    resp.data = data
    return resp.get_response()


@login_required()
def blogs(request):
    """博客管理"""
    user_id = str(request.user.id)
    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    c = RequestContext(request, {
        'profile':profile,
        'siderbar':True,
        'siderbar_name':'sider_blogs',
    })
    return render_to_response('dashboard_blogs.html',c)


@login_required()
def blogs_api(request):
    """博客管理数据"""
    user_id = str(request.user.id)

    if request.POST.get('_method','') == 'delete':
        blog_id = request.POST.get('blog_id','')
        try:
            Blog.objects.filter(id=blog_id).update(is_use=False)
        except:
            traceback.print_exc()

        cur_page = request.GET.get('cur_page', 1)
        datas = Blog.objects.filter(id=user_id,is_use=True).order_by('-created_at')
        paged_datas = Paginator(datas, settings.COUNT_PER_PAGE)
        cur_datas = paged_datas.page(cur_page)
        datas = cur_datas.object_list

        pageinfo = {
            "totalPages": int(paged_datas.num_pages),
            "currentPage": int(cur_page)
        }

        items = []
        for data in datas:
            items.append({
                'blog_id': str(data.id),
                'title': data.title,
                'summary': data.content[:60],
                'tag': data.tag,
                'created_at': data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        resp = jsonresponse.creat_response(200)
        data = {
            'items':items,
            'pageinfo':pageinfo
        }
        resp.data = data
        return resp.get_response()
    else:
        cur_page = request.GET.get('cur_page', 1)

        datas = Blog.objects.filter(user_id=user_id, is_use=True).order_by('-created_at')
        paged_datas = Paginator(datas, settings.COUNT_PER_PAGE)
        cur_datas = paged_datas.page(cur_page)
        datas = cur_datas.object_list

        pageinfo = {
            "totalPages": int(paged_datas.num_pages),
            "currentPage": int(cur_page)
        }

        items = []
        for data in datas:
            items.append({
                'blog_id': str(data.id),
                'title': data.title,
                'summary': data.content[:60],
                'tag': data.tag,
                'created_at': data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        resp = jsonresponse.creat_response(200)
        data = {
            'items': items,
            'pageinfo': pageinfo
        }
        resp.data = data
        return resp.get_response()


@login_required()
def trash(request):
    """垃圾桶"""
    user_id = str(request.user.id)

    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    c = RequestContext(request, {
        'profile':profile,
        'siderbar':True,
        'siderbar_name':'sider_trash',
    })

    return render_to_response('dashboard_trash.html',c)


@login_required()
def trash_api(request):
    user_id = str(request.user.id)
    if request.POST.get('_method', '') == 'undo':
        blog_id = request.POST.get('blog_id', '')
        try:
            Blog.objects.filter(id=blog_id).update(is_use=True)
        except:
            traceback.print_exc()
        cur_page = request.GET.get('cur_page', 1)

        datas = Blog.objects.filter(user_id=user_id, is_use=False).order_by('-created_at')
        paged_datas = Paginator(datas, settings.COUNT_PER_PAGE)
        cur_datas = paged_datas.page(cur_page)
        datas = cur_datas.object_list

        pageinfo = {
            "totalPages": int(paged_datas.num_pages),
            "currentPage": int(cur_page)
        }

        items = []
        for data in datas:
            items.append({
                'blog_id': str(data.id),
                'title': data.title,
                'summary': data.content[:60],
                'tag': data.tag,
                'created_at': data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        resp = jsonresponse.creat_response(200)
        data = {
            'items': items,
            'pageinfo': pageinfo
        }
        resp.data = data
        return resp.get_response()
    elif request.GET:
        cur_page = request.GET.get('cur_page', 1)
        datas = Blog.objects.filter(user_id=user_id, is_use=False).order_by('-created_at')

        paged_datas = Paginator(datas, settings.COUNT_PER_PAGE)
        cur_datas = paged_datas.page(cur_page)
        datas = cur_datas.object_list

        pageinfo = {
            "totalPages": int(paged_datas.num_pages),
            "currentPage": int(cur_page)
        }

        items = []
        for data in datas:
            items.append({
                'blog_id': str(data.id),
                'title': data.title,
                'summary': data.content[:60],
                'tag': data.tag,
                'created_at': data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        resp = jsonresponse.creat_response(200)
        data = {
            'items': items,
            'pageinfo': pageinfo
        }
        resp.data = data
        return resp.get_response()


@login_required()
def comments(request):
    """评论管理"""
    user_id = str(request.user.id)

    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    c = RequestContext(request, {
        'profile':profile,
        'siderbar':True,
        'siderbar_name':'sider_comments',
    })

    return render_to_response('dashboard_comments.html',c)

@login_required()
def comments_api(request):
    pass

@login_required()
def filter(request):
    """过滤器"""
    user_id = str(request.user.id)

    userprofile = UserProfile.objects.filter(user_id=user_id)
    profile = {}
    if userprofile:
        userprofile = userprofile[0]
        profile['nickname'] = userprofile.nickname
        profile['signature'] = userprofile.signature

    c = RequestContext(request, {
        'profile':profile,
        'siderbar':True,
        'siderbar_name':'sider_filter',
    })

    return render_to_response('dashboard_filter.html',c)

@login_required()
def filter_api(request):
    pass