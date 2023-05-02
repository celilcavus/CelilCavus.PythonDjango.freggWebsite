from django.db import models

# Create your models here.
class Home(models.Model):
    Title = models.CharField(max_length=50,null=False)
    SubTitle = models.CharField(max_length=50,null=False)
    Description = models.TextField(max_length=200,null=False,default="")

class About(models.Model):
    Image = models.TextField(max_length=50,null=False)
    Description = models.TextField(max_length=1000,null=False,default="")

class Service(models.Model):
    Icon = models.CharField(max_length=50,null=False)
    Title = models.CharField(max_length=50,null=False)
    Description = models.TextField(max_length=50,null=False,default="")

class Contact(models.Model):
    Name = models.TextField(max_length=50,null=False)
    Email = models.TextField(max_length=50,null=False)
    Message = models.TextField(max_length=50,null=False)