from django.urls import path
from . import views

urlpatterns = (
    path('search/', views.BookSearchView.as_view(), name='search'),
    path('search/results', views.BookSearchResultView.as_view(), name='search_results'),
)
