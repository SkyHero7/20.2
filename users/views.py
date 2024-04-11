from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Product

class UserRegistrationView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Отправить письмо пользователю после успешной регистрации
        send_registration_confirmation_email(user.email)
        return super().form_valid(form)


def send_registration_confirmation_email(email):
    subject = 'Registration Confirmation'
    message = 'Thank you for registering on our website!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)



def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            new_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            user.password = make_password(new_password)
            user.save()
            send_password_reset_email(email, new_password)
            return HttpResponse('Password reset email sent successfully')
        except CustomUser.DoesNotExist:
            return HttpResponse('User with this email does not exist')
    else:
        return render(request, 'users/password_reset.html')

def send_password_reset_email(email, new_password):
    subject = 'Password Reset'
    message = f'Your new password is: {new_password}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price']

    def form_valid(self, form):
        user = self.request.user
        product = form.save(commit=False)
        product.owner = user
        product.save()
        return super().form_valid(form)
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})