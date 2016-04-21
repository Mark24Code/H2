from django.conf.urls import include, url
from django.contrib import admin
from Account import views as account_views
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', account_views.index,name='index'),
    url(r'^login/$', account_views.login),
    # url(r'^logout/$', account_views.logout),
    # url(r'^account/', include('Account.urls')),
]
