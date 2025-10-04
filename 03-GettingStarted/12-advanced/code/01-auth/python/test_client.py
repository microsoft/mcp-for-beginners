# call localhost:8000 with requests.get("http://localhost:8000")
import requests

response = requests.get("http://localhost:8000")
print("Response status code:", response.status_code)
print("Response headers:", response.headers)
print("Response body:", response.text)