
from django.contrib import admin
from django.urls import path
from itspace.views import main 
from django.urls.conf import include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("", main, name="home"),
    path("devices/", include("devices.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += staticfiles_urlpatterns()