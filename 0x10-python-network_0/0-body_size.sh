#!/bin/bash
# Store the URL provided as an argument
url=$1

# Send a request to the URL and store the response body in a temporary file
response=$(curl -sS -s $url)
size=$(echo -n "$response" | wc -c)
# Display the size of the response body
echo "$size"

