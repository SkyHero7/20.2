from django.urls import path
from django.contrib.auth.views import LoginView
from .views import UserRegistrationView, password_reset
from .views import profile

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('password_reset/', password_reset, name='password_reset'),
    path('profile/', profile, name='profile'),

]