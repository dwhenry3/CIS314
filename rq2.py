import requests

try:
    response = requests.get('https://api.github.com', timeout=5)
    response.raise_for_status()  # Raise an error for bad HTTP status
    print(response.json())
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)