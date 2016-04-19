from django.conf.urls import include, url
from django.contrib import admin
from Account import views as account_view
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('Account.urls')),
    # url(r'^login/', account_view.login),
    # url(r'^blogs/', include('Blog.urls')),
]
