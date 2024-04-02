from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]
