from django.contrib.auth.decorators import login_required
from core import jsonresponse
from Like.models import Like


@login_required()
def like_api(request):
    if request.POST.get('_method','') == 'put':
        user_id = str(request.user.id)
        blog_id = request.POST.get("blog_id","")
        print("PUT:user_id",user_id,',blog_id',blog_id)
        try:
            like = Like(
                user_id=user_id,
                blog_id=blog_id)
            like.save()
        except Exception as e:
            print(e)

        resp = jsonresponse.creat_response(200)
        data = {
            # 'url':'/blogs/?id={user_id}'.format(user_id=user_id)
        }
        resp.data = data
        return resp.get_response()

    elif request.POST.get('_method','') == 'delete':
        user_id = str(request.user.id)
        blog_id = request.POST.get("blog_id","")
        print("DELETE:user_id",user_id,',blog_id',blog_id)

        try:
            Like.objects.filter(user_id=user_id,blog_id=blog_id).delete()
        except Exception as e:
            print(e)

        resp = jsonresponse.creat_response(200)
        data = {
            # 'url':'/blogs/?id={user_id}'.format(user_id=user_id)
        }
        resp.data = data
        return resp.get_response()
    elif request.GET:

        user_id = str(request.user.id)
        blog_id = request.GET.get('blog_id','')
        liked = False
        try:
            like_data = Like.objects.filter(blog_id=blog_id).order_by('id')
            like = len(like_data)
            like_user_id = [str(like.user_id) for like in like_data]
            if str(user_id) in like_user_id:
                liked = True
        except:
            like = 0
        resp = jsonresponse.creat_response(200)
        data = {
            'like':like,
            'liked':liked
        }
        resp.data = data
        return resp.get_response()