from django.conf.urls import url
from app_riafy.views import bill_management


urlpatterns = [
    url(r'^api/bill/details/get/$', bill_management.bill_details_get),
    ]