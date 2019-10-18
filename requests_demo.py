import requests
from pprint import pprint

base_url = "https://api.github.com/users/"
user_name = "robnhls"

url = base_url + user_name

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    # pprint(data)
    print("name", data["name"])
    print("location", data["location"])
    print("followers", data["followers"])

else:
    print("there was an issue")
