from urllib.parse import urlencode

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .services import search_books
from .models import Book
from .forms import SearchForm


class BookSearchView(LoginRequiredMixin, FormView):
    template_name = 'books/search.html'
    form_class = SearchForm
    success_url = '/search_results/'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.query = None

    def form_valid(self, form):
        print(form.cleaned_data)
        self.query = form.cleaned_data  # assuming 'query' is a form field
        return super(BookSearchView, self).form_valid(form)

    def get_success_url(self):
        success_url = reverse_lazy('search_results')  # Get base URL for search results

        query_string = urlencode(self.query)
        return f'{success_url}?{query_string}'


class BookSearchResultView(LoginRequiredMixin, ListView):
    model = Book  # Placeholder - We'll fetch data dynamically
    template_name = 'books/search_results.html'
    context_object_name = 'books'
    paginate_by = 15  # Books per page

    def get_queryset(self):
        super().get_queryset()
        search_term = self.request.GET.get('q')
        page = self.request.GET.get('page', 1)

        data = search_books(query=search_term, page=page, max_results=self.paginate_by)

        # Create and return a list of Book objects (adjust if you want to store these in the database)
        books = []

        if 'items' in data:
            for item in data['items']:


                print('item', item)

                book = Book(
                    title=item.get('title', ''),
                    authors=', '.join(item.get('authors', [])),
                    # ...extract other fields as needed
                )
                books.append(book)
        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')
        context['current_page'] = self.request.GET.get('page', 1)
        # context['total_items'] = data.get('totalItems', 0)
        return context

