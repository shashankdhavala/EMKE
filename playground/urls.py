from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.login_user, name='login'),
    path('signup/',views.signup_user, name='signup'),
    path('signup/verify_doctor',views.verify_doctor,name='verify')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)