from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

class UserRegistrationView(FormView):
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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def send_registration_confirmation_email(email):
    subject = 'Registration Confirmation'
    message = 'Thank you for registering on our website!'
    from_email = 'your_email@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
