from django.conf.urls import include, url
from  Blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.blogs,name='blogs'),
    url(r'^api/$', blog_views.blogs_api,name='blogs_api'),
    url(r'^blog/$', blog_views.blog,name='blog'),
    url(r'^blog/api/$', blog_views.blog_api,name='blog_api'),
]
