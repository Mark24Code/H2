from django.conf.urls import include, url
from  Blog import views as BlogViews
urlpatterns = [
    url(r'^$', BlogViews.BlogList),
]
