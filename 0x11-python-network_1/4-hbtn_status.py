#!/usr/bin/python3
"""fetches url with requests"""
import requests


response = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))