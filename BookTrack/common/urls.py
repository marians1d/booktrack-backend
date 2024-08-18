from django.urls import path
from .views import index, Home

urlpatterns = (
    path('', index, name='home_page'),
    path('test/',Home.as_view() , name='test_page'),
)
