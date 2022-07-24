
import requests

from flask import Flask


## GYM ID
id = 1447805280



# Requests data from link
response = requests.get("https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=" +str(id))



# Tests if request was successful
if response.status_code != 200:
    print("Response status was not succesful !! ")



# Transfers data to a json file 
data = response.json()


# Presents data
for item in data["items"]:
    if item["isCurrent"]:
        current_capacity = item["percentage"]


## Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    # return str(current_capacity) + "%"
    return "hi"

# studios/"+str(id)+"/capacity"


# print(current_capacity, "%")