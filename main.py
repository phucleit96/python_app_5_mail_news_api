import requests
from send_email import send_email
import json
import os
from datetime import datetime, timedelta
import calendar

now = datetime.now()

# Subtract one day
one_day_before = now - timedelta(days=1)

# Calculate the last day of the previous month
if one_day_before.month == 1:
    one_month_before = one_day_before.replace(year=one_day_before.year-1, month=12, day=calendar.monthrange(one_day_before.year-1, 12)[1])
else:
    one_month_before = one_day_before.replace(month=one_day_before.month-1, day=calendar.monthrange(one_day_before.year, one_day_before.month-1)[1])

formatted_date = one_month_before.strftime("%Y-%m-%d")



api_key = "532cecc741c2449aa9e590c8fd75c57f"
# api_key = os.getenv('NEWS_API_KEY')

url = f"https://newsapi.org/v2/everything?q=tesla&from={formatted_date}&sortBy=publishedAt&apiKey={api_key}"
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