from django.conf.urls import include, url
from Square import views as square_views

urlpatterns = [
    url(r'^$', square_views.squares,name='squares'),
    url(r'^api/$', square_views.squares_api,name='squares_api'),
    # url(r'^square/$', square_views.square,name='square'),
    # url(r'^square/api/$', square_views.square_api,name='square_api'),
]
