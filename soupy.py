#pip install requests beautifulsoup4
from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome to the Test Page</h1>
    <p class="description">This is a sample page.</p>
    <a href="http://example.com/page1">Link 1</a>
    <a href="http://example.com/page2">Link 2</a>
  </body>
</html>
"""

# Parse HTML
#soup = BeautifulSoup(html_doc, 'html.parser')
soup = BeautifulSoup(html_doc, 'html5lib')

# Get the title
print(soup.title.string)

# Get the first paragraph text
print(soup.p.text)

# Get all links
for link in soup.find_all('a'):
    print(link.get('href'))