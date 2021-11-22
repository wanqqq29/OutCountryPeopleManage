from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import outPeople.views

urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('Tinfo/',outPeople.views.Tinfo),
    path('Sinfo/',outPeople.views.Sinfo),
    path('auth/',include('rest_auth.urls')),
    path('CsR/',outPeople.views.get_csrf_token),
    path('login/',outPeople.views.login)
    # path('fields/',outPeople.views.Allfileds)
]

#http://127.0.0.1:8888/accounts/register/