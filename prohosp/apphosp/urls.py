from django.urls import path
from. import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('dep/',views.departments,name='departments'),
    path('appointment/',views.appointment,name='appointment'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
]