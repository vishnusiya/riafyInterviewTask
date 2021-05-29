from django.conf.urls import url
from django.conf.urls import url
from app_frontend.views import admin_site

urlpatterns = [
  url(r'^$', admin_site.home),
  url(r'^home/$', admin_site.home),
]
