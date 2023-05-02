from django.contrib import admin
from . import models
# Register your models here.



class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','Title')

class About(admin.ModelAdmin):
    list_display = ("id","Description")

class Service(admin.ModelAdmin):
    list_display = ("id","Title","Description")

class Contact(admin.ModelAdmin):
    list_display = ("id","Name","Message")

admin.site.register(models.Home,HomeAdmin)
admin.site.register(models.About,About)
admin.site.register(models.Service,Service)
admin.site.register(models.Contact,Contact)