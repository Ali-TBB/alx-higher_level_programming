#!/usr/bin/python3
"""Fetches a URL and handles HTTP errors."""
import sys
import urllib.request
import urllib.error


def main(url):
    """
    Fetches a URL and handles HTTP errors.

    Args:
        url (str): The URL to fetch.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
