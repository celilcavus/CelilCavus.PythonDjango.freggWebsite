from django.shortcuts import render
from .models import Home,About,Contact,Service
# Create your views here.


def index(request):
    try:
        home = Home.objects.all()
        context = {
        'home':home
        }
        print(home.values_list())
    except Exception as ex:
        print(ex)
    return render(request,'index.html',context)