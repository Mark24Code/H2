from django.conf.urls import include, url
from django.contrib import admin
from Account import views as account_view
urlpatterns = [
    url(r'^$', account_view.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('Account.urls')),
]
