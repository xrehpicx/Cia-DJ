"""cia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include
from django.conf.urls import url

from allauth.account.views import confirm_email
from api.views import attend,something,getUser,activate,VeryNewCustomRegisterView

from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset_confirm,password_reset_complete

from api.views import HelloView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sarath/<uid>/<token>/',something),
    path('getUser/',getUser),
    path('hello/', HelloView.as_view(), name='hello'),
   # url(r'^api/v1/rest-auth/registration/account-confirm-email/(?P<key>[-/\w]+)/$', confirm_email, name='account_confirm_email'), 
#url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#        activate, name='activate'),
    re_path('api/(?P<version>(v1|v2))/', include('api.urls')),
    url(r'activate/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<uidb64>[0-9A-Za-z_\-]+)/$',
        activate, name='act'),
    url(r'^act/<uidb64>/<token>/$',
        activate, name='activate'),
       
   
     url(r'register/$', VeryNewCustomRegisterView.as_view(), name='rest_register'),
    url(r'^account_inactive/$',TemplateView.as_view(),name = 'account_inactive'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'reset/confirm/done/$', password_reset_complete, name='password_reset_complete'),
    #url(r'rest-auth/registration/ ^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
    


]
