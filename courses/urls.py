from django.urls import path

from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('aboutUS',views.AboutUs,name='aboutme'),
    path('coursesDisp',views.allCourses,name='coursesdisp'),
    path('guide_to_learn_more',views.homepage,name='guide_to_learn_more'),
    path('communitysection',views.community,name='community'),
]