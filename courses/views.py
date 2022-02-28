from django.shortcuts import render
from django.http import HttpResponse
from .models import FeedBack,CustomerAccount,store_courses
from datetime import datetime


# Create your views here.
def homepage(request):

    Accname=request.user.username
    parms={'username':Accname}
    return (render(request, 'index.html',parms))



def AboutUs(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("Email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        
        feedback=FeedBackUs(name=name,email=email,phone=phone,desc=desc,date=datetime.now())
        feedback.save()
    Accname=request.user.username
    
    parms={'username':Accname}
    return (render(request,'feedback.html',parms))




def allCourses(request):
    Accname=request.user.username
    courses= store_courses.objects.all()

    parms={'username':Accname,'coursedata':courses}
    return (render(request,'allcourses.html',parms))

def community(request):
    Accname=request.user.username
    parms={'username':Accname}
    return (render(request,'Community.html',parms))

    pass