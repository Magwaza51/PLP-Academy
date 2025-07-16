# go to a website and return results
import requests

response = requests.get("https://www.bbc.co.uk")
print(response.text)