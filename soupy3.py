# Find all paragraphs with phone numbers using a regular expression
import requests
import re
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://phenrylaw.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    phones_text = soup.find_all(string=re.compile(r'\(?\d{1,3}[-.) ]?\d{3}[-. ]?\d{4}'))
    for phone_text in phones_text:
        phones = re.findall(r'\(?\d{1,3}[-.) ]?\d{3}[-. ]?\d{4}', phone_text)
        for phone in phones:
            print(phone)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)