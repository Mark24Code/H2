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

def index(request):
    """
    首页
    """
    return render_to_response('index.html',{})


def login(request):
    """
    登录和注册
    """
    #注册
    if request.POST.get('_method','') == 'put':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        try:
            User.objects.create_user(username=username,password=password)
        except:
            traceback.print_exc()

        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/login/'
        }
        resp.data = data
        return resp.get_response()
    #登录
    elif request.POST.get('_method','') == 'post':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request,user)
            request.session['user_id'] = user.id
            reload_url = user_router(user)
            data = {
                'url':reload_url
            }
            resp = jsonresponse.creat_response(200)
            resp.data = data
            return resp.get_response()
    else:
        return render_to_response('login.html',{})


def logout(request):
    """
    注销
    """
    del request.session['user_id']
    auth.logout(request)

    return render_to_response('logout.html',{})


def user_router(user):
    """
    角色跳转
    """
    if user.is_superuser:
        return "/blogs/"
    else:
        return "/blogs/"

@login_required()
def account(request):
    """
    用户个人资料
    """
    if request.POST.get('_method','') == 'put':
        user_id = str(request.user.id)
        nickname = request.POST.get('nickname','')
        signature = request.POST.get('signature','')
        phone = request.POST.get('phone','')
        remark = request.POST.get('remark','')
        profile = UserProfile(
            user_id=user_id,
            nickname=nickname,
            signature=signature,
            phone=phone,
            remark=remark)
        profile.save()

        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/accounts/account/?id={user_id}'.format(user_id=user_id)
        }
        resp.data = data
        return resp.get_response()
    if request.POST.get('_method','') == 'post':
        user_id = str(request.user.id)
        nickname = request.POST.get('nickname','')
        signature = request.POST.get('signature','')
        phone = request.POST.get('phone','')
        remark = request.POST.get('remark','')
        profile = UserProfile.objects.filter(user_id=user_id)
        profile.update(
            user_id=user_id,
            nickname=nickname,
            signature=signature,
            phone=phone,
            remark=remark)

        resp = jsonresponse.creat_response(200)
        data = {
            'url':'/accounts/account/?id={user_id}'.format(user_id=user_id)
        }
        resp.data = data
        return resp.get_response()

    else:
        user_id = str(request.user.id)
        userprofile = UserProfile.objects.filter(user_id=user_id)
        profile = {}
        if userprofile:
            userprofile = userprofile[0]
            profile['nickname'] = userprofile.nickname
            profile['signature'] = userprofile.signature
            profile['phone'] = userprofile.phone
            profile['remark'] = str(userprofile.remark)
        c = RequestContext(request, {
            'profile':profile
        })

        return render_to_response('account.html',c)
