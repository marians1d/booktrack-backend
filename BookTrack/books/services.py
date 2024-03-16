import requests


def search_books(query):
    api_key = 'YOUR_API_KEY'
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        return None
