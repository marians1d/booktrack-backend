from django.shortcuts import redirect
from django.urls import reverse_lazy


class RedirectAuthenticatedUserMixin:
    DEFAULT_REDIRECT = 'home_page'
    redirect_to = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_to or reverse_lazy(self.DEFAULT_REDIRECT))
        return super().dispatch(request, *args, **kwargs)
