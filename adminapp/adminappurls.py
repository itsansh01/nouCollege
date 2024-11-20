from django.urls import path
from . import views
#write your urls path here
urlpatterns=[
    path('dashboard/',views.dashboard,name='dashboard'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('viewcopmlaints/',views.viewcomplaints,name='viewcomplaints'),
    path('studymaterial/',views.studymaterial,name='studymaterial'),
    path('viewmaterial/',views.viewmaterial,name='viewmaterial'),
    path('move/',views.move,name='move'),
    # path('newsandevents/',views.newsandevents,name='newsandevents'),
]