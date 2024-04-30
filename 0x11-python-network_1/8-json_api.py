#!/usr/bin/python3
"""Sends a POST request to url with a letter as a parameter."""
import sys
import requests


def search_user(letter):
    """
    Sends a POST request to url with a letter as a parameter.

    Args:
        letter (str): The letter to search for.

    Returns:
        str: The formatted response.
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            return "[{}] {}".format(json_response['id'], json_response['name'])
        else:
            return "No result"
    except ValueError:
        return "Not a valid JSON"


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    print(search_user(letter))
