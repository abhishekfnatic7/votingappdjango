from django.urls import path
from . import views
urlpatterns = [
    path('',views.studentsignup,name='studentsignup'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('studentlogout',views.studentlogout,name='studentlogout'),
    path('home',views.home,name='home'),
    # path('checkvote',views.checkvote,name='checkvote'),
    path('vid',views.vid,name='vid'),
    # path('first',views.first,name='first'),
    
]
