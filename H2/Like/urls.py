from django.conf.urls import include, url
from  Like import views as like_views
urlpatterns = [
    # url(r'^$', like_views.likes,name='likes'),
    # url(r'^api/$', like_views.likes_api,name='likes_api'),
    # url(r'^like/$', like_views.like,name='like'),
    url(r'^like/api/$', like_views.like_api,name='like_api'),
]
