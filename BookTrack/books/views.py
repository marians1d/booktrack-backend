import math
from datetime import datetime
from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView

from .forms import SearchForm
from .models import Book, UserBook
from .services import search_books


class BookSearchView(LoginRequiredMixin, FormView):
    template_name = 'books/search.html'
    form_class = SearchForm
    success_url = '/search_results/'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.query = None

    def form_valid(self, form):
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
    custom_paginate_by = 10
    total_pages = 0

    @staticmethod
    def convert_published_date(date_string):
        for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
            try:
                return datetime.strptime(date_string, fmt).date()
            except ValueError:
                continue
        return None

    def get_queryset(self):
        super().get_queryset()
        search_term = self.request.GET.get('q')
        page = self.request.GET.get('page', 1)

        data = search_books(query=search_term, page=page, max_results=self.custom_paginate_by)

        # Create and return a list of Book objects (adjust if you want to store these in the database)
        books = []

        self.total_pages = math.ceil(data['totalItems'] / self.custom_paginate_by)

        if 'items' in data:
            for item in data['items']:
                info = item.get('volumeInfo', None)

                industry_identifiers = info.get('industryIdentifiers', [])

                isbn = None
                for identifier in industry_identifiers:
                    if identifier['type'] == 'ISBN_13':
                        isbn = identifier['identifier']

                images = info.get('imageLinks', {})

                date_string = info.get('publishedDate', None)

                published_date = self.convert_published_date(date_string)

                try:
                    book = Book.objects.get(external_id=item.get('id', None))
                except Book.DoesNotExist:
                    book = Book(
                        external_id=item.get('id', None),
                        title=info.get('title', ''),
                        subtitle=info.get('subtitle', ''),
                        description=info.get('description', ''),
                        authors=', '.join(info.get('authors', [])),
                        categories=', '.join(info.get('categories', [])),
                        published_date=published_date,
                        isbn=isbn,
                        page_count=info.get('pageCount', None),
                        small_cover_link=images.get('smallThumbnail', None),
                        cover_link=images.get('thumbnail', None)
                    )

                    book.save()

                books.append(book)
        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')
        context['current_page'] = int(self.request.GET.get('page', 1))
        context['total_pages'] = self.total_pages
        context['paginate_by'] = self.custom_paginate_by
        return context


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/details.html'
    context_object_name = 'book'


class UserBookCreateView(LoginRequiredMixin, CreateView):
    model = UserBook

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
