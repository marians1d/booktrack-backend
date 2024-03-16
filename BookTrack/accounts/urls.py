from django.urls import path
from .views import RegistrationView, LoginUserView, LogoutUserView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user')
]
