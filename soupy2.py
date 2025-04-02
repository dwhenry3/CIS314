import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://phenrylaw.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup.head)
    #print(soup.head.contents[1])
    print(soup.title.contents[0])
    
    '''# Example: Extract the title of the page
    title = soup.title.string
    print("Page Title:", title)
    
    # Example: Extract all links
    for link in soup.find_all('a'):
        print("Link text:", link.text)
        print("URL:", link.get('href'))
    
    # Example: Extract all headings
    for header in soup.find_all(['h1', 'h2', 'h3']):
        print(f"{header.name}: {header.text.strip()}")'''
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
