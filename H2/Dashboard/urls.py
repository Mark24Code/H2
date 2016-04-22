from django.conf.urls import include, url
from  Dashboard import views as dashboard_views
urlpatterns = [
    url(r'^$', dashboard_views.dashboard,name='dashboard'),
]
