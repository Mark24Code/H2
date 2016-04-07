from django.conf.urls import include, url
from  Blog import views as BlogViews
urlpatterns = [
    url(r'^blog/', BlogViews.Blog),
    url(r'^list/', BlogViews.BlogList),
    url(r'^edit/', BlogViews.BlogEdit),
]
