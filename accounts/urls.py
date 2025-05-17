from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('resend-verification/', views.reverify, name='resend_verification'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('final-reset/', views.final_reset, name='final_reset'),
]
