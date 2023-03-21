from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('passwordreset/', views.PasswordResetView.as_view(), name='password-reset'),
]
