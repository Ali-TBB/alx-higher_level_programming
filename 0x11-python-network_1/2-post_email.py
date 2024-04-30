#!/usr/bin/python3
"""Sends an email via a POST request to the specified URL."""
import sys
import urllib.parse
import urllib.request


def send_email(url, email):
    """
    Sends an email via a POST request to the specified URL.

    Args:
        url (str): The URL to fetch.
        email (str): The email to send.
    """
    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    print(data)
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(request.read().decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_email(url, email)
