import requests

url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'

local_file_name = "nasa.pdf"

with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_file_name, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            # print(".", end=" ")
            if chunk:
                f.write(chunk)

print("File Written")
