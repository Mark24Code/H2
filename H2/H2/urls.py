from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('Account.urls')),
    url(r'^index/', include('Account.urls')),
    url(r'^blogs/', include('Blog.urls')),
]
