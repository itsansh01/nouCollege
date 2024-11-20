from django.urls import path
from . import views
#write your urls path here
urlpatterns=[

    path('',views.parent,name='parent'),
    path('index/',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('courses/',views.courses,name='courses'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('contactus/',views.contactus,name='contactus'),
]