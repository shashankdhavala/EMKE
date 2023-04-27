from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.login_user, name='login'),
    path('signup/',views.signup_user, name='signup'),
    path('signup/verify_doctor',views.verify_doctor,name='verify')
]