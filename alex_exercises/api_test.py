#/usr/bin/python3
import sys, json, requests

var_dict = {
        "lat": 40.71,
        "lon": -74
        }
URL = "http://api.open-notify.org/astros.json"

if len(sys.argv) > 1:
    URL = sys.argv[1]
    if len(sys.argv) > 2:
        var_dict["lat"], var_dict["lon"] = sys.argv[2:4]

def jprint (obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get(URL, params=var_dict)
print("Status code: ", response.status_code)
print(response.json())

jprint(response.json())

if len(sys.argv) > 1:
    jprint(response.json()['response'])

