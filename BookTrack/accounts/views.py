from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from .forms import RegistrationForm
from .mixins import RedirectAuthenticatedUserMixin

UserModel = get_user_model()


class RegistrationView(RedirectAuthenticatedUserMixin, views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(RedirectAuthenticatedUserMixin, auth_views.LoginView):
    template_name = 'accounts/login.html'
    # form_class = LoginForm

    next_page = reverse_lazy('home_page')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('home_page')
