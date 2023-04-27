from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.login_doctor, name='login'),
    path('signup/',views.signup_doctor, name='signup'),
    path('signup/verify_doctor',views.verify_doctor,name='verify'),
    path('doc_home/',views.verify_login,name='verify_login'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('view_patients/',views.view_patients,name='view_patients'),
    path('save_patients/',views.save_patient,name='save_patient')


]