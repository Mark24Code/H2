from django.conf.urls import include, url
from django.contrib import admin
from Account import views as AccountViews
urlpatterns = [
    url(r'^$', AccountViews.index),
    url(r'^index/$', AccountViews.index),
    url(r'^login/$', AccountViews.login),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^account/', include('Account.urls')),
]
