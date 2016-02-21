from django.conf.urls import include, url
from django.contrib import admin
import Blog

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('Blog.urls')),
]
