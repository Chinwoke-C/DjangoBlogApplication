from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class PasswordResetView(generic.UpdateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'accounts/password_reset.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
