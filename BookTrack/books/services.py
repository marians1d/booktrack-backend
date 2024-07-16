import requests
from django.conf import settings


def search_books(query, filter_by='intitle', print_type='books', order_by='relevance', page=1, max_results=15):
    api_key = settings.GOOGLE_BOOKS_API_KEY

    base_url = 'https://www.googleapis.com/books/v1/volumes'

    q = f'{filter_by}:{query}'

    params = {
        'q': q,
        'key': api_key,
        'orderBy': order_by,
        'printType': print_type,
        'startIndex': (int(page) - 1) * max_results,
        'maxResults': max_results
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()

        return data
    else:
        return None
