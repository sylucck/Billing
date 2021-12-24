from django.urls import path
from . import views
from django.conf.urls import url, include
from accounts.views import dashboard,register
   


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    
]
