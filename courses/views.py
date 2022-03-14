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

    return(render(request,'aboutus.html'))

def feedback(request):
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


# def search(request):
#     try:    
#         query = request.GET.get('search')
#         allCourse = []
#         catprods = Product.objects.values('subject', 'id')
#         cats = {item['subject'] for item in catprods}
#         for cat in cats:
#             prodtemp = Product.objects.filter(subject=cat)
#             prod = [item for item in prodtemp if searchMatch(query, item)]

#             n = len(prod)
#             nSlides = n // 4 + ceil((n / 4) - (n // 4))
#             if len(prod) != 0:
#                 allCourse.append([prod, range(1, nSlides), nSlides])
#         params = {'allCourse': allCourse, "msg": ""}
#         if len(allCourse) == 0 or len(query)<4:
#             params = {'msg': "Please make sure to enter relevant search query"}
#         return render(request, 'shop/search.html', params)
#     except:
#         return render(request, 'shop/search.html', params)


# def searchMatch(query, item):
#     '''return true only if query matches the item'''
#     if query in item.course_title.lower() or query in item.subject.lower():
#         return True
#     else:
#         return False


def searchpage(request):
#------------------------------------------------
    # Accname=request.user.username
    # query = request.GET.get('search')
    # allCourse = []
    # catcorse = store_courses.objects.values('subject', 'course_title')
    # cats = {item['subject'] for item in catcorse}
    # for cat in cats:
    #     prodtemp = store_courses.objects.filter(subject=cat)
    #     prod = [item for item in prodtemp if searchMatch(query, item)]

    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     if len(prod) != 0:
    #         allCourse.append([prod, range(1, nSlides), nSlides])

    # params = {'username':Accname,'allCourse': allCourse, "msg": ""}
    # if len(allCourse) == 0 or len(query)<4:
    #     params = {'msg': "Please make sure to enter relevant search query",'username':Accname}
#--------------------------------------------------
    Accname=request.user.username
    parms={'username':Accname}
    return (render(request,'search.html',parms))
