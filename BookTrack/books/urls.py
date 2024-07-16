from django.urls import path
from . import views

urlpatterns = (
    path('<int:pk>/details', views.BookDetailView.as_view(), name='book_details'),
    path('<int:pk>/create', views.BookDetailView.as_view(), name='book_create_view'),
    path('search/', views.BookSearchView.as_view(), name='search'),
    path('search/results', views.BookSearchResultView.as_view(), name='search_results'),
)
