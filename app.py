# == Imported modules
# ======================================================

import requests                 # To be able to request data from the API
from flask import Flask         # To be able to create the flask app endpoint
from flask_cors import CORS
import json                     # To be able to export data in json format




# == Flask application
# ======================================================

app = Flask(__name__)
CORS(app)




# == Get all studios
# ======================================================

@app.route("/studios")
def get_all_studios():
    """1. Feature. Returns all studios data as a json file."""

    # Request studio data from link   
    response = requests.get("https://rsg-group.api.magicline.com/connect/v1/studio?studioTags=AKTIV-391B8025C1714FB9B15BB02F2F8AC0B2")

    # Transform JSON into python format
    data = response.json()


    # Create list
    studios_list = list()

    for studio in data:

        studios_list.append(
            {
                "id": studio["id"],
                "name": studio["studioName"],
                "address": {
                    "city": studio["address"]["city"],
                    "zip": studio["address"]["zipCode"],
                    "street": studio["address"]["street"]
                }
            })

    # Transform data back into JSON format
    studios_json = json.dumps(studios_list)

    # Return JSON as endpoint
    return studios_json




## == Get capacity for specific studio
## ======================================================

@app.route("/studios/<studio_id>/capacity")
def get_capacacity_by_id(studio_id):
    """2. Feature. Returns studio capacity data as a json file."""

    # Request capacity data from link
    response = requests.get("https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=" + str(studio_id))

    # Transform JSON into python format
    data = response.json()

    # Create dictionary
    capacity_dict = dict()

    # Searches for capacity information in json data
    for item in data["items"]:
        if item["isCurrent"]:

            # Returns current capacity in percentage
            capacity_dict["current capacity in percentage"] = item["percentage"]
    
    # Transform data back into JSON format
    capacity_json = json.dumps(capacity_dict)

    # Return JSON as endpoint
    return capacity_json

