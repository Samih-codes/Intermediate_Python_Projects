import requests
from datetime import datetime

USERNAME = "enter_your_own"
TOKEN = "enter_your_own"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id":GRAPH_ID,
	"name":"Quran Graph",
	"unit": "min",
	"type": "float",
	"color": "shibafu",
}

headers = {
	"X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_config = {
	"date": today.strftime("%Y%m%d"),
	"quantity": "40"
}

# response = requests.post(url=pixel_add_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_edit_endpoint = f"{pixel_add_endpoint}/{today.strftime('%Y%m%d')}"

pixel_edit_config = {
	"date": today.strftime("%Y%m%d"),
	"quantity": input("How much time did you spend reading Quran today? ")
}

response = requests.put(url=pixel_edit_endpoint, json=pixel_edit_config, headers=headers)
print(response.text)

pixel_delete_endpoint = f"{pixel_edit_endpoint}"

# response = requests.delete(url=pixel_edit_endpoint, headers=headers)
# print(response.text)