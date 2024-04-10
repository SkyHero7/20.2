from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from .models import CustomUser
from django.conf import settings

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
