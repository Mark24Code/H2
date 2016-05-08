from django.conf.urls import include, url
from Comment import views as comment_views

urlpatterns = [
    # url(r'^$', comment_views.comments,name='comments'),
    url(r'^api/$', comment_views.comments_api,name='comments_api'),
    # url(r'^comment/$', comment_views.comment,name='comment'),
    url(r'^comment/api/$', comment_views.comment_api,name='comment_api'),
]
