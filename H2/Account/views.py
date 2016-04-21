from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import Group, User
from Account.models import UserProfile
from django.contrib.auth.decorators import login_required
import json


def login(request):
    if request.POST:
        print('login:POST')
        if request.POST.get('_method') == 'put':
            print('api/login:PUT')
            return HttpResponseRedirect(reverse('index'))
        if request.POST.get('_method') == 'post':
            print('api/login:POST')
            return HttpResponseRedirect(reverse('index'))
    else:
        print('login:GET')

        return render_to_response('login.html',{})

# def logout(request):
#     if request.POST:
#         print('login:POST')
#     else:
#         print('login:GET')
#         return render_to_response('logout.html',{})



def index(request):
    if request.POST:
        print('index:POST')
    else:
        print('index:GET')
        return render_to_response('index.html',{})






# def login(request):
#     '''
#     账号注册与登录
#     '''
#     if request.POST:
#         print('AAAAAAAAAA')
#         return HttpResponseRedirect('/')
#         ##注册
#         #if request.POST.get('_method','')=="put":
#         #    print('api/account:PUT')
#         #    username = request.POST['username']
#         #    password = request.POST['password']
#         #    try:
#         #        user = User.objects.create_user(username = username,password=password)
#         #    except Exception as err:
#         #        print(err)
#         #    return HttpResponseRedirect('/login/')


#         ##登录
#         #if request.POST.get('_method','')=='post':
#         #    return HttpResponseRedirect('/')
#             #print('api/account:POST')
#             #username = request.POST['username']
#             #password = request.POST['password']

#             #user = auth.authenticate(username=username,password=password)
#             #print(user)
#             #if user and user.is_active:
#             #    auth.login(request,user)
#             #    request.session['user_id'] = user.id
#             #    print(9999)
#             #    #return render_to_response('index.html',{})
#             #    return user_router(user)

#     print('account:GET')
#     return render_to_response('login.html',{})
#     #return render_to_response('index.html',{})

# def user_router(user):
#     '''
#     基于不同角色跳转
#     '''
#     print(44444444)
#     if user.is_superuser:
#         return HttpResponseRedirect('/')
#     else:
#         print(111111144444444)
#         return HttpResponseRedirect('/')


# def logout(request):
#     '''
#     注销
#     '''
#     del request.session['user_id']
#     auth.logout(request)
#     return HttpResponseRedirect('/login/')

# @login_required()
# def index(request):
#     print('index:')
#     return render_to_response('index.html',{})