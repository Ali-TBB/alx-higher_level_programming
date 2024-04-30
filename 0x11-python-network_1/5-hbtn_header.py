#!/usr/bin/python3
""" displays the value of the X-Request-Id
variable found in the header of the response
"""
import sys
import requests


def main(url):
    """
    displays the value of the X-Request-Id
    variable found in the header of the response.

    Args:
        url (str): The URL to fetch.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
