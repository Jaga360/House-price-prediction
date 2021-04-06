from flask import Flask, request
import json
import pickle
import numpy as np

app = Flask(__name__)

__location=None

@app.route('/getLocation')
def getLocation():
    with open('artifacts/house_prediction_columns.json' , ) as f:
        location =  json.load(f)
        global __location
        __location = location["data_columns"][3:]
    return json.dumps(__location)


@app.route('/predict', methods=['POST'])
def predict():
    with open('artifacts/house_price_prediction.json' , 'rb') as f:
        model= pickle.load(f)

    #to get user values from the html form, use same name as in input tag    
    x=np.zeros(__location + 3)
    x[0]=int(request.form['bhk'])
    x[1]=float(request.form['sqft'])
    x[2]=int(request.form['bath'])
    loc=request.form['location']

    try:
        locIndex = __location.index(loc)
    except:
        locIndex=-1

    x[locIndex]=1

    return round(model.predict([x]),2)



if __name__ == '__main__':
    app.run()