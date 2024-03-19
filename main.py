# Import necessary modules
import requests
from send_email import send_email
import random
from datetime import datetime, timedelta
import calendar
import os


# Function to calculate the date one month and one day before the current date
def calculate_date():
    # Get the current date and time
    now = datetime.now()
    # Subtract one day
    one_day_before = now - timedelta(days=1)
    # If the current month is January
    if one_day_before.month == 1:
        # Set the month to December of the previous year
        one_month_before = one_day_before.replace(year=one_day_before.year - 1, month=12,
                                                  day=calendar.monthrange(one_day_before.year - 1, 12)[1])
    else:
        # Subtract one month
        one_month_before = one_day_before.replace(month=one_day_before.month - 1,
                                                  day=
                                                  calendar.monthrange(one_day_before.year, one_day_before.month - 1)[1])
    # Return the date formatted as "yyyy-mm-dd"
    return one_month_before.strftime("%Y-%m-%d")


# Get the API key
api_key = os.getenv('NEWS_API_KEY')
# List of possible topics
topic_list = ["technology", "python", "research", "data-science", "positivity", "creativity", "google", "stock", "ufo", "artificial-intelligence"]
# Choose a random topic
topic = random.choice(topic_list)
# Calculate the date for the news articles
formatted_date = calculate_date()
# Construct the URL for the API request
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"from={formatted_date}&"
       f"language=en&"
       f"sortBy=publishedAt&"
       f"apiKey={api_key}")

# Make a request to the API
response = requests.get(url)
# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Parse the JSON response
content = response.json()

# Start constructing the email body with the subject line
body = f"Subject: {topic.capitalize()}'s News" + "\n"
# Add each article to the email body
for article in content['articles'][:20]:
    if article['title'] and article['description']:
        body += (article['title'] + "\n" + article['description']
                 + "\n" + article['url'] + 2 * "\n")

# Encode the email body as UTF-8
body = body.encode('utf-8')

# Send the email
send_email(message=body)
