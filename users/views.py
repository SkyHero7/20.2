from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView


class UserRegistrationView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # Делаем пользователя неактивным, пока не подтвердит почту
        user.save()

        return redirect(self.success_url)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Проверка, существует ли пользователь с таким именем
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                # Вывод ошибки или выполнение других действий
                # Например, перенаправление на страницу с сообщением об ошибке
                return render(request, 'error.html', {'message': 'Это имя пользователя уже занято. Пожалуйста, выберите другое имя пользователя.'})
            else:
                user = form.save()
                login(request, user)
                # Отправить письмо пользователю после успешной регистрации
                send_registration_confirmation_email(user.email)
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def send_registration_confirmation_email(email):
    # Здесь вы можете настроить отправку письма подтверждения регистрации
    subject = 'Registration Confirmation'
    message = 'Thank you for registering on our website!'
    from_email = 'your_email@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
