from flask import Flask, request
import json
import pickle

app = Flask(__name__)

@app.route('/getLocation')
def getLocation():
    with open('artifacts/house_prediction_columns.json' , ) as f:
        location =  json.load(f)
   
    return json.dumps(location["data_columns"][3:])




if __name__ == '__main__':
    app.run()