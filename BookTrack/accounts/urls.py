from django.urls import path
from .views import RegistrationView, LoginUserView, LogoutUserView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user')
]
