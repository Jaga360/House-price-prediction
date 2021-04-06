import json


def getLocation():
    with open('artifacts/house_prediction_columns.json' , ) as f:
        location =  json.load(f)
    
    print(type(location))
    return 'Hello, World!'


getLocation()