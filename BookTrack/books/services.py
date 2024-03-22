import requests
from django.conf import settings


def search_books(query, order_by='relevance', page=1, max_results=15):
    api_key = settings.GOOGLE_BOOKS_API_KEY

    base_url = 'https://www.googleapis.com/books/v1/volumes'

    params = {
        'q': query,
        'key': api_key,
        'startIndex': (int(page) - 1) * max_results,
        'maxResults': max_results
    }

    if order_by:
        params['orderBy'] = order_by

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()

        return data
    else:
        return None
