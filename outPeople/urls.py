from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),

]

#http://127.0.0.1:8888/accounts/register/