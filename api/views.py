from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,EventsSerializer,NewsSerializer,AttendRegisterSerializer,ProjectSerializer,InterestGroupSerializer,NewRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_auth.registration.views import RegisterView
from .models import User,Events,News,AttendRegister,Project,InterestGroup,InterestGroupMember
from . import serializers
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import UserSignUpForm,MyRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User





from rest_framework import status
from rest_framework.response import Response
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from rest_auth.views import LoginView,PasswordResetView
from rest_auth.registration.views import RegisterView
import requests
import json
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm


from rest_auth.app_settings import (
    TokenSerializer,  UserDetailsSerializer, JWTSerializer, create_token
)
from rest_auth.utils import jwt_encode
from .models import User,Visioneer
from django.views.generic.edit import CreateView, DeleteView, UpdateView



from cia import settings
from django.core.mail import EmailMessage

from .forms import UserSignUpForm,VisioneerForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.context_processors import csrf



#json
def getjsonmodel(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    data = open('cia/data.json').read()
    
    jsonData = json.loads(data) 
    

    return JsonResponse(jsonData,safe=False)

#json
def getjsonmodel2(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    data = open('cia/data2.json').read()
    
    jsonData = json.loads(data) 
    

    return JsonResponse(jsonData,safe=False)


@login_required
def visioneerview(request):
    if request.method == 'POST':
        print("VISIONEER")
        
        #d = dict(request.POST)
        print(request.POST)
        #d['passwordhashfunction'] = 'MD5'
        #d['orgunitpath'] = 'uk'
        #d['orgunitpath'] = 'uk'
        form = VisioneerForm(request.POST)
        if form.is_valid():
            print("Correct")
            form.save()
            return redirect('index')
    else:
        form = VisioneerForm()
    context = {"form":form}
    return render(request,'visioneer.html',context)


class VisioneerCreate(CreateView):
    model = Visioneer
    fields='__all__'

@login_required
def profile(request):
    return render(request,'registration/profile.html')


# DJAGO USER REGISTER
""" def register(request):
    
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user =authenticate(username=form.username,password=password)
            login(request,user)
            return redirect('index')

    else:
        form = UserSignUpForm()
    context = {"form":form}
    return render(request,'registration/register.html',context)
        """
#@api_view(['POST'])
""" def register(request):
    if request.method == 'POST':
        print("POST")
        print(request)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        usn = request.POST.get('usn')
        dept = request.POST.get('dept')
        ut_id = request.POST.get('ut_id')
        phone_number = request.POST.get('phone_number')
        d={}
        d['username']=username
        d['email']=email
        d['password1']=password1
        d['password2']=password2
        d['usn']=usn
        d['dept']=dept
        d['ut_id']=ut_id
        d['phone_number']=phone_number

        r = requests.post(url = 'http://test.ciadev.ninja:8000/register/', data = d)
        print("this is r",r)
        #data = json.dumps(r.content)
        #print(data)
    

        
    else :
        return render(request, 'registration/register.html')    """

""" """ 
#WORKING REGISTER 2.0
def register(request):
    a = 1
    #if request.user.is_authenticated():
    if a>2:
        return HttpResponseRedirect('/user/')
    else:
        print("yo")
        if request.method == 'POST':
            print("Its post")
            
            try:
                form = MyRegistrationForm(request.POST)
                if form.is_valid():
                    print("form is valid")
                    form.save()
                    user = User.objects.get(email=request.POST.get('email'))
                    user.is_active = False
                    user.save()
                    mail_subject = 'Activate your CIA account.'
                    to_email = request.POST.get('email')
                    message = render_to_string('acc_active_email.html', {
                    'user': user, 'domain':'test.ciadev.ninja',
                    'uid': user.pk,
                    'token': account_activation_token.make_token(user),

                    })
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return render(request,'mainsite.html')
            except:
                return render(request,'oops.html')
            return render(request,'oops.html')
        else:
            print("yo2")
            context = {}
            context.update(csrf(request))
            context['form'] = MyRegistrationForm()
            return render(request, 'register.html', context) 

def loginPage(request):
    if request.method == 'POST':
        print("POST")
        print(request)
        email = request.POST.get('email')
        password = request.POST.get('password')
        d={}
        d['email']=email
        d['password']=password
        r = requests.post(url = 'http://139.59.61.35:8000/login/', data = d)
        data = json.dumps(r.content)
        print(data)
    

        
    else :
        return render(request, 'loginPage.html')


def index(request):
    """View function for home page of site."""
    '''
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }'''

    # Render the HTML template index.html with the data in the context variable
    #return render(request, 'index.html', context=context)
    return render(request, 'index.html')

#from rest_framework import serializers

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['POST'])
def getUser(request):
    print(request.data)
    #token = Token.objects.get(key=request.data['token'])
    return Response({"response"})

class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CustomRegisterView(RegisterView):
        queryset = User.objects.all()


class ListInterestGroupView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = InterestGroup.objects.all()
    serializer_class = InterestGroupSerializer

class ListEventsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Events.objects.all().order_by('-e_date')
    serializer_class = EventsSerializer

class ListNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-p_datetime')
    serializer_class = ProjectSerializer


'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['POST'])
def attend(request,version):
    if request.method == 'POST':
        print(request.body)
        try:
            token = Token.objects.get(key=request.data['token'])
            event = Events.objects.get(e_code=request.data['e_code'])
            print(event)
            print(token.user)
            #attendregister = AttendRegister.objects.filter(e_id=event,u_id=token.user).count()  
            attendregister = AttendRegister.objects.filter(e_id=event,u_id=token.user).count()
            print('DINA:')
            print(attendregister)
        except:
            return Response({"response":False})
        '''try: 
            

            #total_count = AttendRegister.objects.filter(u_id=token.user).count()
            print('SSSS'.attendregister)
            #return Response({"response":False})
        except:
            return Response({"response":False})
            print('')'''
       # print(attendregister)
        
        print(event.e_score)
        print(token.user)
        if event.e_state:
            if attendregister == 0:
                serializer = AttendRegister(e_id=event,u_id=token.user)
                #if serializer.is_valid():
                serializer.save()
                #event = Events.objects.get()
                #attend_register = AttendRegister.
                #return Response({'token': token.key, 'id': token.user.username})
                return Response({'response':True})
        else: 
            return Response({'response':False})

'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['POST'])
def getstats(request,version):
    if request.method == 'POST':
        print(request.body)
        try:
            token = Token.objects.get(key=request.data['token'])
            total_count = AttendRegister.objects.filter(u_id=token.user).count()
            allevents = AttendRegister.objects.filter(u_id=token.user)
            score_sum =0
            for i in allevents:
                score_sum=score_sum+i.e_id.e_score
            return Response({"response":True,"score_sum":score_sum,"total_count":total_count})
            #print(sum)
            #print('vndo'.AttendRegister.objects.filter(u_id=token.user))
            
            
        except:
            return Response({"response":False})
        return Response({"response":False})
@api_view(['GET'])
def getmembers(request,version):
    try:
        ig = InterestGroup.objects.get(id=request.GET['id'])
        members = InterestGroupMember.objects.filter(ig_id=ig)
        users = {}
        count = 1
        for member in members:
            print(member.user.username)
            users[count]= member.user.username
            count =count+1
        #data = serializers.serialize('json', self.get_queryset())
        #data = serializers.serialize('json', users)
        #return HttpResponse(data, content_type="application/json")
        print(users)
        
        

      #  users = []
        #print(InterestGroupMemberSerializer(members))
       # for member in members:
       #     users.add(member)
        #print(users)
        return Response({"response":True, "members":users})
    except:
        return Response({"response":False})


# CUSTOM LOGIN VIEW 
class LoginUserDetailView(LoginView):
    def get_response_serializer(self):
        if getattr(settings, 'REST_USE_JWT', False):
            response_serializer = JWTSerializer
        elif getattr(settings, 'REST_USE_TOKEN', True):
            response_serializer = TokenSerializer
        else:
            response_serializer = UserDetailsSerializer
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data['user']

        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(self.user)
        elif getattr(settings, 'REST_USE_TOKEN', True):
            self.token = create_token(self.token_model, self.user,
                                      self.serializer)

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': self.token
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        elif getattr(settings, 'REST_USE_TOKEN', True):
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.user,
                                          context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)

### NEXT CHECK - WORKING CUSTOM LOGIN - OVERRIDING get_response from LOGIN-VIEW
class CustomLoginView(LoginView):
    '''def get_response(self):
        orginal_response = super().get_response()
        print(orginal_response['key'])
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response'''
    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': self.token
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False):
            from rest_framework_jwt.settings import api_settings as jwt_settings
            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime
                expiration = (datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(jwt_settings.JWT_AUTH_COOKIE,
                                    self.token,
                                    expires=expiration,
                                    httponly=True)
        #return response
        orginal_response = response
        #orginal_response = super().get_response()
        print(orginal_response)
        mydata = {"username": self.user.username,"email": self.user.email, "status": "success",'non_field_errors': ['NONE']}

        orginal_response.data.update(mydata)
        if self.user.is_active:
            return orginal_response
        else:
            mydata = {"username": '',"email": '', "status": "Please activate your account"}
            return orginal_response

## CUSTOM REGISTER VIEW

class VeryNewCustomRegisterView(RegisterView):
    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {"detail": _("Verification e-mail sent.")}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }
            return JWTSerializer(data).data
        else:
            #return TokenSerializer(user.auth_token).data
            orginal_response = TokenSerializer(user.auth_token).data
            print("ORIGINAL RESPONSE")
            print(orginal_response)
            #orginal_response = super().get_response()
            mydata = {"username": user.username,"email": user.email, "status": "ACTIVATE"}
            #current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':'current_site.domain',
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your CIA account.'
            to_email = user.email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            print('MY DATA')
            print(mydata)
            orginal_response.update(mydata)
            print("ORIGINAL RESPONSE")
            print(orginal_response)
            return orginal_response



def activate(request, uidb64, token):
    try:
        uid = uidb64
        print('Inside ',uid)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['GET'])
def something(request,uid, token ):
    try:
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
#    return Response({"uid":uid,"token":token})


def testReset(request):
    return render(request,'test.html')