import requests

# Send a GET request to a website
response = requests.get('https://phenrylaw.com')

#Print the status code and content
print (response.status_code)
print ("-----------------------")
#print (response.text)

response = requests.post('https://postman-echo.com/post','Hello CIS 314')

print(response.status_code)
print ("-----------------------")
print (response.text)