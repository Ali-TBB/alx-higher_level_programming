#!/usr/bin/python3
"""
load_from_json_file function
function that creates an Object from a “JSON file”.
Author:
[ali debbache]
Date:
[2024/02/06]
"""

from sys import argv
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

file_name = "add_item.json"

try:
    existing_items = load_from_json_file(file_name)
except FileNotFoundError:
    existing_items = []

for arg in argv[1:]:
    existing_items.append(arg)

save_to_json_file(existing_items, file_name)
