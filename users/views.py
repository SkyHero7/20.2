from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .forms import CustomUserCreationForm

class UserRegistrationView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # Делаем пользователя неактивным, пока не подтвердит почту
        user.save()

        # Отправка письма для верификации
        send_mail(
            'Подтвердите вашу почту',
            'Пожалуйста, подтвердите вашу почту, перейдя по ссылке.',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        return redirect(self.success_url)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после успешной регистрации
            return redirect('login')  # Перенаправление на страницу логина
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})