from django.conf.urls import url, include

urlpatterns = [
    url("", include("app_riafy.urls.bill_management")),
]
