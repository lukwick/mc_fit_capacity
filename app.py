# == Imported modules
# ======================================================

import requests                 # To be able to request data from API
from flask import Flask         # To be able to create flask app endpoint
from flask_cors import CORS     # Additional modules for flask app
import json                     # To be able to export data in json format




# == Flask application
# ======================================================

app = Flask(__name__)
CORS(app)




# == Functions
# ======================================================

def get_data(api_link):
    """Get data of API. Returns api response."""
    return requests.get(api_link)

def parse_data(response):
    """Takes json file. Transforms it. Returns python data."""
    return response.json()

def dumps_json(selected_data):
    """Takes python data. Transforms it. Returns json data."""
    return json.dumps(selected_data)



# == Get all studios
# ======================================================

@app.route("/studios")
def get_all_studios():
    """Returns all studios data as json."""

    api_link = "https://rsg-group.api.magicline.com/connect/v1/studio?studioTags=AKTIV-391B8025C1714FB9B15BB02F2F8AC0B2"

    def select_data(response):
        """Takes data. Returns selected data."""

        # Create output list
        studios_list = list()

        # Loop through all studios
        for studio in response:
            
            # Append each studio with selected data to list, then return list
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
                
        return studios_list

    # Merge all functions together
    return dumps_json(select_data(parse_data(get_data(api_link))))




## == Get capacity for specific studio
## ======================================================

@app.route("/studios/<studio_id>/capacity")
def get_capacacity_by_id(studio_id):
    """Returns studio capacity data as json."""

    api_link = "https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=" + str(studio_id)

    def select_data(studio_hours):
        """Takes data. Returns selected data."""

        # Loop through each studio hour
        for hour in studio_hours["items"]:

            # If hour is current hour, then return value
            if hour["isCurrent"]:
                return {"current": hour["percentage"]}

    # Merge all functions together
    return dumps_json(select_data(parse_data(get_data(api_link))))

