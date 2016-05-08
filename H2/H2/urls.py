from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Account import views as account_views
from Dashboard import views as dashboard_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', account_views.index,name='index'),
    url(r'^login/$', account_views.login,name='login'),
    url(r'^logout/$', account_views.logout,name='logout'),
    url(r'^accounts/', include('Account.urls')),
    url(r'^blogs/', include('Blog.urls')),
    url(r'^comments/', include('Comment.urls')),
    url(r'^squares/', include('Square.urls')),
    url(r'^dashboard/', dashboard_views.dashboard,name='dashboard'),
]

urlpatterns += staticfiles_urlpatterns()