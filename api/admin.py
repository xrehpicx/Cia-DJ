from django.contrib import admin
from .models import User,Events,News,AttendRegister,UserType,Dept,Project,Visioneer
# Register your models here.
admin.site.register(User)
admin.site.register(Events)
admin.site.register(News)
admin.site.register(AttendRegister)
admin.site.register(UserType)
admin.site.register(Dept)
admin.site.register(Project)
admin.site.register(Visioneer)
