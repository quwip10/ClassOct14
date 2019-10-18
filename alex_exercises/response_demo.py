import requests
from pprint import pprint

base_url = "https://api.github.com/users/"
user_name = "quwip10"

url = base_url + user_name

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
#    pprint(data)
    print("Name:", data["name"])
    print("Location:", data["location"])
else:
    print("there was an issue")