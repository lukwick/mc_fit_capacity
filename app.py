

# == IMPORTED MODULES
# ======================================================

# To be able to request data from the API
import requests

# To be able to create the flask app endpoint
from flask import Flask

# To be able to export data in json format
import json



# == FLASK
# ======================================================


## 0. FLASK APPLICATION
## ==================================

app = Flask(__name__)



## 1. SHOW ALL STUDIOS
## ==================================

# HTTP:127.0.0.1:5000/studios
@app.route("/studios")

def get_all_studios():
    """1. Feature. Returns all studios data as a json file."""

    # Request gym data from link   
    response = requests.get("https://rsg-group.api.magicline.com/connect/v1/studio?studioTags=AKTIV-391B8025C1714FB9B15BB02F2F8AC0B2")

    # Transform JSON into python format
    data = response.json()

    # Create dictionary
    gyms_dict = {}

    # Select Gym ID as key and Gym Name as value
    for gym in data:
        # gyms_dict[gym["id"]] = gym["studioName"]
        gyms_dict[gym["studioName"]] = {"id": gym["id"]}

    # Sort Gym Name
    gyms_dict_sorted = {}
    for gym in sorted(gyms_dict):
        gyms_dict_sorted[gym] = gyms_dict[gym]

    # print(gyms_dict_sorted)


    # Transform data back into JSON format
    gyms_json = json.dumps(gyms_dict_sorted, indent=2)


    # print(gyms_json)



    # Return JSON as endpoint
    return gyms_json





## 2. SHOW CAPACITY FOR ALL STUDIOS
## ==================================

# HTTP:127.0.0.1:5000/studios
@app.route("/studios/<id>")

def get_capacacity_by_id(id):
    """2. Feature. Returns studio capacity data as a json file."""

    # Request capacity data from link
    response = requests.get("https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=" +str(id))

    # Transform JSON into python format
    data = response.json()

    # Read information
    capacity_dict = {}

    for item in data["items"]:
        if item["isCurrent"]:
            capacity_dict["current"] = item["percentage"]
    
    # Transform data back into JSON format
    capacity_json = json.dumps(capacity_dict)

    # Return JSON as endpoint
    return capacity_json