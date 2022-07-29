

# IMPORTED MODULES
# ----------------------------------------------------------

import requests             # To be able to request data from the API
from flask import Flask     # To be able to create the flask app endpoint
import json                 # To be able to export data in json format



# FLASK
# ---------------------------------------------------------

## FLASK APPLICATION
## -------------------

app = Flask(__name__)



## SHOW ALL STUDIOS
## --------------------

@app.route("/studios")
def get_all_studios():
    # todo: implement proper fetching of all gym ids
    return "['123']"



## SHOW CAPACITY FOR ALL STUDIOS
## --------------------

@app.route("/studios/<id>/capacity")
def get_capacacity_by_id(id):

    # Request data from link
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