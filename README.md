# News Email Sender

This project is a Python script that fetches news articles from the NewsAPI based on a randomly selected topic from a predefined list. It then sends an email containing the top 20 articles (if available) to a specified email address.
![Demo](https://i.imgur.com/CZ2la6C.gif)
## Features

- Fetches news articles from NewsAPI.
- Selects a topic randomly from a predefined list.
- Sends an email with the top 20 articles related to the selected topic.

## Usage

Set the following environment variables:

- `NEWS_API_KEY`: Your NewsAPI key.
- `PASSWORD`: The password for the email account from which emails will be sent.

Run the script:


## Email Configuration

The script uses SMTP to send emails. The current configuration is set to use Gmail's SMTP server. If you want to use another email provider, you need to change the `host` and `port` in the `send_email` function in `send_email.py`.

