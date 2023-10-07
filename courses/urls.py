from django.urls import path

from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('aboutUS',views.AboutUs,name='aboutme'),
    path('feedback',views.feedback,name='feedback'),
    path('coursesDisp',views.allCourses,name='coursesdisp'),
    # path('search',views.searchpage,name='searchcourse'),
    path('communitysection',views.community,name='community'),
    path('search', views.search_courses, name='search_courses'),
]