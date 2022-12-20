# mc_fit_capacity

# Goal
- Show current capacity of selected studio
- Frontend: iOS via ReactNative
- Backend: HTTP API via Python

# Features
- List all McFit group gym studios 
- Show current capacity of selected studio

# End user journey
1. User sees list of all studios
2. Clicks on studio 
3. Sees capacity

![McFit capacity website](/application_preview.png)

# Request journey
1. Get list of studios with IDs `GET /studios`
2. User clicks 
3. Request capacity for that id `GET /studios/[ID]/capacity`

# Server endpoints

## 1. Get all studios

`GET /studios`

Returns JSON:

```json
[
    {
        "id": 1674653140,
        "name": "McFIT Hannover-Vahrenheide",
        "address": {
            "city": "Hannover",
            "zip": "30179",
            "street": "Vahrenwalder Str."
        }
    }
]
```


## 2. Get capacity for selected studio

`GET /studios/[ID]/capacity`

Returns JSON:

```json
{
    "current": 46,
}
```

## Endpoints

- [Gym ID List](`https://rsg-group.api.magicline.com/connect/v1/studio?studioTags=AKTIV-391B8025C1714FB9B15BB02F2F8AC0B2`)
- [Example McFit endpoint](`https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=1447805280`)


# Getting started

## Install

### Backend

Install packages:

```sh
# Install python
apt-get install python3

# Install pip
apt install python3-pip

# Check version
python3 --version
pip --version

# Install flask
pip install Flask-Cors

# Check install
python3 -m pip show Flask-Cors
```

Create environment:

```sh
# Create project folder
mkdir myproject

# Go into folder
cd myproject

# Create venv folder in the project
python3 -m venv venv
```

### Frontend

```sh
# Install node
apt install nodejs

# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash

#  Check versions
node --version
nvm --version
npm --version
```

## Running applications

### Backend

```sh
# Start flask
flask run

# missing
```


### Frontend

```sh
# Start npm
npm start

# missing
```