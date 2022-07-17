
import requests


# Requests data from link
response = requests.get("https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=1447805280")
# print(type(response)) # Class: requests.models.Response


# Tests if request was successful
if response.status_code != 200:
    print("Response status was not succesful !! ")


# Transfers data to a json file 
data = response.json()
print(type(data)) # Class: dict 


# Presents data
for item in data["items"]:
    if item["isCurrent"]:
        current_capacity = item["percentage"]

print(current_capacity, "%")



