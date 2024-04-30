import urllib.request

# Replace 'url_here' with the URL you want to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Open the URL
with urllib.request.urlopen(url) as response:
    # Read the body of the response
    body = response.read().decode('utf-8')  # Assuming UTF-8 encoding, adjust if needed
    print(body)
