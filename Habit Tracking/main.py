import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hbxiahyyi0bjbcbjajd"
USERNAME = "belac"
GRAPH_ID = "codegraph"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime(year=2022, month=8, day=13)

graph_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0.8",

}

# response = requests.post(url=pixel_creation_endpoint, json=graph_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220814"
update_data = {
    "quantity": "2.3",
}
response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
print(response.text)