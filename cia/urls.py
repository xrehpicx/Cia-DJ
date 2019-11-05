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
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,re_path, include
from django.conf.urls import url

from allauth.account.views import confirm_email
from api.views import attend,something,getUser,activate,VeryNewCustomRegisterView,testReset,CustomLoginView,register,profile,VisioneerCreate,visioneerview

from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset_confirm,password_reset_complete

from api.views import HelloView,index,loginPage
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, RedirectView
from . import settings


urlpatterns = [

    #FOR WEB
    path('admin/', admin.site.urls), # ADMIN url
   #url(r'^$', TemplateView.as_view(template_name="home.html"), name='hom   e'),
    path('accounts/',include('django.contrib.auth.urls')), # TO GET ALL USER URLS
    path('',TemplateView.as_view(template_name="mainsite.html"),name="index"),
    path('register/',register,name="register"),
    path('profile/',profile,name='profile'),
    #path('visioneer/add/', VisioneerCreate.as_view(), name='author-add'),
    path('visioneer/', visioneerview, name='visioneer'),
   

    

    


     url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),



    #FOR MOBILE
    url(r'^loginpage/',loginPage,name="loginpage"),
    
    url(r'reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'), # POST RESET MAIL 
    url(r'reset/confirm/done/$', password_reset_complete, name='password_reset_complete'),
    re_path('api/(?P<version>(v1|v2))/', include('api.urls')),
    url(r'register/$', VeryNewCustomRegisterView.as_view(), name='rest_register'),
    url(r'^login/$', CustomLoginView.as_view(), name='main_login'),
    url(r'^account_inactive/$',TemplateView.as_view(),name = 'account_inactive'), # no idea y but register needs this
    path('activate/<uid>/<token>/',something),     # ACTIVATEING ACCOUNT - LINK MAILED 

    path('rest-auth/login/', LoginView.as_view(), name='rest_login'),

    #url(r'^act/<uidb64>/<token>/$', activate, name='activate'),
    #path('hello/', HelloView.as_view(), name='hello'),
    #path('getUser/',getUser),
    #path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password-reset/',testReset,name='password_reset'), #CUSTOM RESET PAGE


]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

