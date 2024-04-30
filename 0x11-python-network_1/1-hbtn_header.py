#!/usr/bin/python3
import sys
import urllib.request


def main(url):
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)