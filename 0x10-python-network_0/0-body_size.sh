#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided as an argument
url=$1

# Send a request to the URL and store the response body in a temporary file
response=$(curl -sS $url)

# Get the size of the response body in bytes
size=$(echo -n "$response" | wc -c)

# Display the size of the response body
echo "$size bytes"

# Remove the temporary file
rm -f response_body.tmp

