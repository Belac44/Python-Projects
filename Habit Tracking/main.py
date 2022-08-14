import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hbxiahyyi0bjbcbjajd"
USERNAME = "belac"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "codegraph",
    "name": "Coding graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)