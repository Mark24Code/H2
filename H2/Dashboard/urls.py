from django.conf.urls import include, url
from  Dashboard import views as dashboard_views
urlpatterns = [
    # url(r'^$', dashboard_views.dashboard,name='dashboard'),
    url(r'^stat/$', dashboard_views.stat,name='dashboard_stat'),
    url(r'^comments/$', dashboard_views.comments,name='dashboard_comments'),
    url(r'^blogs/$', dashboard_views.blogs,name='dashboard_blogs'),
    url(r'^trash/$', dashboard_views.trash,name='dashboard_trash'),
    url(r'^filter/$', dashboard_views.filter,name='dashboard_filter')
]
