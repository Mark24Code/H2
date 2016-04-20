from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from Account.models import UserProfile
from django.contrib.auth.decorators import login_required
import json

def login(request):
    '''
    账号注册与登录
    '''
    #注册
    if request.POST.get('_method','')=="put":
        try:
            print('api/account:PUT')
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create(username = username)
            user.set_password(password)
            user.save()
            data={"code":200}
            return HttpResponseRedirect('/login/')
        except Exception as err:
            print(err)
            data = {"code":500}
            return JsonResponse(data)

    #登录
    if request.POST.get('_method','')=='post':
        try:
            print('api/account:POST')
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username,password=password)
            print('sadddddddddddd')
            print(user)
            if user is not None:
                print(11111111111111)
                if user.is_active:
                    print(33333333333333)
                    request.session['user_id'] = user.id
                    print(333444444444444)
                    return HttpResponseRedirect('/index/')
                else:
                    return HttpResponseRedirect('/login/')
            else:
                print(2222222222222222)
                return HttpResponseRedirect('/login/')

        except Exception as err:
            print(err)
            return HttpResponseRedirect('/login/')

    print('account:GET')
    return render_to_response('login.html',{})

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


def index(request):
    print(999999)
    return render_to_response('index.html',{})