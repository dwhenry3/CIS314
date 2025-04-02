from bs4 import BeautifulSoup
import re

html_doc = """
<html>
  <body>
    <p>Email: test@example.com</p>
    <p>Email: sample@example.org</p>
    <p>Phone: (123)456-7890</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Find all paragraphs with emails using a regular expression
emails = soup.find_all(string=re.compile(r'\(?\d{1,3}[-.) ]?\d{3}[-. ]?\d{4}'))
for email in emails:
    print(email)
