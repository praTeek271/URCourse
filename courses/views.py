from django.shortcuts import render
from django.http import HttpResponse
from .models import FeedBack, CustomerAccount, store_courses
from datetime import datetime

def homepage(request):
    Accname = request.user.username
    parms = {'username': Accname}
    return render(request, 'index.html', parms)

def AboutUs(request):
    return render(request, 'aboutus.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("Email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        
        feedback = FeedBack(name=name, email=email, phone=phone, desc=desc, date=datetime.now())
        feedback.save()
    Accname = request.user.username
    parms = {'username': Accname}
    return render(request, 'feedback.html', parms)

def allCourses(request):
    Accname = request.user.username
    courses = store_courses.objects.all()
    courses = courses[:16]
    parms = {'username': Accname, 'coursedata': courses}
    return render(request, 'allcourses.html', parms)

def community(request):
    Accname = request.user.username
    parms = {'username': Accname}
    return render(request, 'Community.html', parms)

def searchpage(request):
    query = request.GET.get('search')
    course_found = []

    if query:
        course_found = store_courses.objects.filter(course_title__icontains=query)

    Accname = request.user.username
    parms = {'username': Accname, 'searchdata': course_found}
    return render(request, 'search.html', parms)


def search_courses(request):
    query = request.GET.get('search')
    course_found = []

    if query:
        course_found = store_courses.objects.filter(course_title__icontains=query)
    if len(course_found) == 0:
        course_found = store_courses.objects.all()[:16]
    Accname = request.user.username
    parms = {'username': Accname, 'coursedata': course_found, 'query': query}
    return render(request, 'search.html', parms)