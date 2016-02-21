from django.conf.urls import include, url
from django.contrib import admin
from Account import views as AccountViews
urlpatterns = [
    url(r'^$', AccountViews.index),
]
