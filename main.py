import requests
import json
import os

api_key = "532cecc741c2449aa9e590c8fd75c57f"
# api_key = os.getenv('NEWS_API_KEY')
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-18&sortBy=publishedAt&apiKey={api_key}"
# Make a request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# Access the article titles and description:
for article in content['articles']:
    print(article['title'])
    print(article['description'])