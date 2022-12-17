# README

## Goal
- Shows current capacity of selected studio
- Frontend: iOS via ReactNative
- Backend: HTTP API via Python

## Features
- studio selection
    - list ALL studios 
    - allow to filter by city name
- Capacity
    - --> show current capacity of selected studio

## End User Journey
1. User sees list of all studios
2. Clicks on studio 
3. Sees capacity

## Request journey
1. get list of studios with IDs `GET /all-gyms`
2. user clicks 
3. request capacity for that id `GET /studios/[ID]/capacity`

## Server Endpoints
### 1. Get all studios

`GET /studios`

Returns JSON:

```json
{name: "McFIT Berlin"
    {   id: 123456,
    }
}
```


### 2. Get the capacity for selected studio

`GET /studios/[ID]/capacity`

Returns JSON. Example: 

```json
{
    current: 46,
}
```



## Example McFit endpoint:
`https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles[studioId]=1447805280`


## Gym ID List
`https://rsg-group.api.magicline.com/connect/v1/studio?studioTags=AKTIV-391B8025C1714FB9B15BB02F2F8AC0B2`



