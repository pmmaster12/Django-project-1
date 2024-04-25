from django.http import HttpResponse
import datetime
from django.shortcuts import render
def home(request):
    date=datetime.datetime.now()
    print("test fucntion called from view")
    return render(request,"home.html",{})
def about(request):
    return render(request,"about.html",{})
def services(request):
   return HttpResponse("<h1> this is services page </h1>")



    