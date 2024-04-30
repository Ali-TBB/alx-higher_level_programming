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
    try:
        response = requests.get(url)
        print(requests)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
