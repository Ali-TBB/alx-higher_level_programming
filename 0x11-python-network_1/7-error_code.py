#!/usr/bin/python3
"""Fetches a URL and handles HTTP errors."""
import sys
import requests


def main(url):
    """
    Fetches a URL and handles HTTP errors.

    Args:
        url (str): The URL to fetch.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(response.text)
        print(" Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
