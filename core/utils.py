import os
os.environ['NEWSAPI_KEY'] = '62dbe69db627457987d3640ae314656a'
import requests

api_key = os.environ['NEWSAPI_KEY']


def get_latest_news():
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['articles']
    









