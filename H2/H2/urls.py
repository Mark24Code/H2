from django.conf.urls import include, url
from django.contrib import admin
from Account import views as account_views
from Blog import views as blog_views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', account_views.index,name='index'),
    url(r'^login/$', account_views.login,name='login'),
    url(r'^logout/$', account_views.logout,name='logout'),
    url(r'^accounts/', include('Account.urls')),
    url(r'^blogs/', include('Blog.urls')),
]
