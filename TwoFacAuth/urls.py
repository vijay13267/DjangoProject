from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('TwoFactAuth/', views.temp_here, name='temp_here'),
    path('VerifyOTP/', views.verify_otp, name='verify_otp'),
]
