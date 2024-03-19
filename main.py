import requests
from send_email import send_email
import json
import os

api_key = "532cecc741c2449aa9e590c8fd75c57f"
# api_key = os.getenv('NEWS_API_KEY')

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-19&sortBy=publishedAt&apiKey={api_key}"
# Make a request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# Access the article titles and description:
body = ""
for article in content['articles']:
    title = article['title'] if article['title'] is not None else ""
    description = article['description'] if article['description'] is not None else ""
    body += title + "\n" + description + 2*"\n"

body = body.encode('utf-8')

send_email(message=body)