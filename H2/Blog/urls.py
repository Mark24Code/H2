from django.conf.urls import include, url
from  Blog import views as blog_views
urlpatterns = [
    url(r'^$', blog_views.blogs),
    url(r'^blog/', blog_views.blog),
]
