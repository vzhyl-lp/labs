import requests

url = "https://student.lpnu.ua/"

response = requests.get(url)

print(response.text)