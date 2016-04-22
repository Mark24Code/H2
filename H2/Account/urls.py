from django.conf.urls import include, url
from django.contrib import admin
from Account import views as account_views
urlpatterns = [
    url(r'^account/$', account_views.account,name='account'),
    # url(r'^api/', account_views.api_account),
]
