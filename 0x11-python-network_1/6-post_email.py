#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as
a parameter and displays the body of the response."""
import sys
import requests


def send_email(url, email):
    """
    Sends an email via a POST request to the specified URL.

    Args:
        url (str): The URL to send the email to.
        email (str): The email content.

    Returns:
        str: The body of the response.
    """
    email_data = {'email': email}
    response = requests.post(url, data=email_data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    send_email(url, email)
