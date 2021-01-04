"""
Definition of urls for E_Com.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', auth_view.LoginView.as_view(template_name = 'app/login.html'	), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name = 'app/password_reset_form.html', email_template_name = 'app/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'), name='password_reset_complete'),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name = 'app/password_change_form.html'), name='password_change'),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(template_name = 'app/password_change_done.html'), name='password_change_done'),
]
