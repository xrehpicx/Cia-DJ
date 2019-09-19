from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists, get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from phonenumber_field.modelfields import PhoneNumberField

from .models import User,Events,UserType,UserTypeRegister
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password','usn','dept','user_t')
        #fields = '__all__'
    def create(self, validated_data):
        user = User(**validated_data)
       # user.__setattr__('is_staff',True)
        # Hash the user's password.
        user.set_password(  ['password'])
        user.save()
        return user

class UserSerializer2(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password','usn','dept','user_t')
        #fields = '__all__'
'''   def create(self, validated_data):
        user = User(**validated_data)
       # user.__setattr__('is_staff',True)
        # Hash the user's password.
        user.set_password(  ['password'])
        user.save()
        return user'''
''' def save(self, validated_data):
        user = User(**validated_data)
       # user.__setattr__('is_staff',True)
        # Hash the user's password.
        user.set_password(  ['password'])
        user.save()
        return user
'''


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    usn = serializers.CharField(required=True)
    
    

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'name': self.validated_data.get('name', ''),
                'usn' : self.validated_data.get('usn',''),
               
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.address = self.cleaned_data.get('usn')
#user.user_type = self.cleaned_data.get('user_type')
        user.save()
        return user

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','name','usn')
        read_only_fields = ('email',)

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("e_id","e_state","e_title","e_date",'e_start_time','e_end_time','e_venue','e_organizer','e_description','e_score','e_registration_link','e_photos_link','e_medium_link')


class UserTypeSerializer(serializers.ModelSerializer):
   # ut_id = serializers.SerializerMethodField()
    #def get_id(self, obj):
     #  return getattr(obj, 'ut_id', 1)
    class Meta:
        model = UserType()
        fields = ('ut_id','ut_name')





#using this for user type id  to be validated
class RegisterSerializerCustom(serializers.Serializer):
    
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    usn = serializers.CharField(required=True)
    user_t = serializers.IntegerField(write_only=True)
    #user_type = PrimaryKeyRelatedField()
   

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        '''if data['password'] != data['password'] :
            raise serializers.ValidationError(_("The two password fields didn't match."))\
        #checking here for user type 
        if data['ut_type'] == 0:
            raise serializers.ValidationError(_("You cannot register as superuser"))'''
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            
            
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user



# THIS FOR SURE WORKS BRO
class UserSerializerMain(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password','usn','dept','user_t')
        write_only_fields = ('password',)
       # read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            usn = validated_data['usn'],
            
            #first_name=validated_data['first_name'],
            #last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            'usn': self.validated_data.get('usn', ''),
        }
            
    def save(self, request):
        adapter = get_adapter()
        print(request)
        user = adapter.new_user(request)
        print(user.username)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)

        setup_user_email(request, user, [])
        return user


class NewRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    usn = serializers.CharField(required=True)
    dept = serializers.IntegerField(required=True)
    ut_id = serializers.IntegerField(required=True)
    phone_number = serializers.CharField(required=True)
    
   # user_t = serializers.IntegerField(write_only=True)
    #user_type = PrimaryKeyRelatedField()
  #  email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
   # first_name = serializers.CharField(required=True, write_only=True)
    #last_name = serializers.CharField(required=True, write_only=True)
    #address = serializers.CharField(required=True, write_only=True)
    #password1 = serializers.CharField(required=True, write_only=True)
    #password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            #'last_name': self.validated_data.get('last_name', ''),
            #'address': self.validated_data.get('address', ''),
            #'user_type': self.validated_data.get('user_type', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'usn': self.validated_data.get('usn', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'ut_id': self.validated_data.get('ut_id', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        #user.address = self.cleaned_data.get('usn')

        #user.user_type = self.cleaned_data.get('user_type')

        user.save()
        return user