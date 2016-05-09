from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.conf import settings

from core import jsonresponse
from Account.models import UserProfile
from Blog.models import Blog

@login_required()
def squares(request):
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
        profile['avatar'] = userprofile.avatar

    c = RequestContext(request, {
        'profile':profile
    })
    return render_to_response('squares.html',c)

@login_required()
def squares_api(request):
    if request.GET:
        user_id = request.GET.get('user_id')
        cur_page = request.GET.get('cur_page',1)

        datas = Blog.objects.all().filter(is_use=True).order_by('-created_at')

        user_ids = [data.user_id for data in datas]
        users = UserProfile.objects.all()
        user_id2avatar = {}
        for user in users:
            user_id2avatar[str(user.user_id)] = str(user.avatar)

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
                'avatar':user_id2avatar[str(data.user_id)],
                'blog_id':str(data.id),
                'title':data.title,
                'summary':data.content[:60],
                'tag':data.tag,
                'created_at':data.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        resp = jsonresponse.creat_response(200)
        data = {
            'items':items,
            'pageinfo':pageinfo
        }
        resp.data = data
        return resp.get_response()
#
#
#
#
# @login_required()
# def blog(request):
#     user_id = str(request.user.id)
#     userprofile = UserProfile.objects.filter(user_id=user_id)
#     profile = {}
#     if userprofile:
#         userprofile = userprofile[0]
#         profile['nickname'] = userprofile.nickname
#         profile['signature'] = userprofile.signature
#
#     if request.GET.get('edit'):
#         user_id = request.GET.get('id','')
#         blog_id = request.GET.get('blog_id','')
#         blog_data = Blog.objects.filter(id=blog_id,user_id=user_id)
#         blog = {}
#         if blog_data:
#             blog_data = blog_data[0]
#             blog['title'] = blog_data.title
#             blog['content'] = blog_data.content
#         c = RequestContext(request, {
#             'blog':blog,
#             'profile':profile
#         })
#         return render_to_response('blog.html',c)
#     elif request.GET.get('blog_id'):
#         user_id = request.GET.get('id','')
#         blog_id = request.GET.get('blog_id','')
#         blog_data = Blog.objects.filter(id=blog_id,user_id=user_id)
#         blog = {}
#         if blog_data:
#             blog_data = blog_data[0]
#             blog['title'] = blog_data.title
#             blog['content'] = blog_data.content
#         c = RequestContext(request, {
#             'blog':blog,
#             'frozen':True,
#             'profile':profile
#         })
#         return render_to_response('blog.html',c)
#
#     c = RequestContext(request, {
#         'profile':profile
#     })
#     return render_to_response('blog.html',c)
# @login_required()
# def blog_api(request):
#     if request.POST.get('_method','') == 'put':
#         user_id = str(request.user.id)
#         blog_title = request.POST.get('blog_title','')
#         blog_content = request.POST.get('blog_content','')
#
#         blog = Blog(
#             user_id=user_id,
#             title=blog_title,
#             content=blog_content)
#         blog.save()
#         blog_id = str(blog.id)
#
#         resp = jsonresponse.creat_response(200)
#         data = {
#             'url':'/blogs/?id={user_id}'.format(user_id=user_id)
#         }
#         resp.data = data
#         return resp.get_response()
#
#     elif request.POST.get('_method','') == 'post':
#         user_id = str(request.user.id)
#         blog_id = request.POST.get('blog_id',0)
#         blog_title = request.POST.get('blog_title','')
#         blog_content = request.POST.get('blog_content','')
#
#         blog = Blog.objects.filter(id=blog_id,user_id=user_id)
#         blog.update(
#             title=blog_title,
#             content=blog_content)
#         resp = jsonresponse.creat_response(200)
#         data = {
#             'url':'/blogs/blog/?id={user_id}&blog_id={blog_id}'.format(user_id=user_id,blog_id=blog_id)
#         }
#         resp.data = data
#         return resp.get_response()