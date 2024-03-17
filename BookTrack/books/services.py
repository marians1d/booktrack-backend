import requests
from django.conf import settings


def search_books(query):
    api_key = settings.GOOGLE_BOOKS_API_KEY
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        return None
