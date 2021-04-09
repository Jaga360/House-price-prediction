from flask import Flask, request
import json
import pickle
import numpy as np

app = Flask(__name__)

#list of locations
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
    global __location
    getLocation()

    with open('artifacts/house_price_prediction.pickle' , 'rb') as f:
        model= pickle.load(f)

    # to get user values from the html form, use same name as in input tag 
    x=np.zeros(len(__location) + 3)
    x[0]=request.form['bhk']
    x[1]=request.form['sqft']
    x[2]=request.form['bath']
    loc=request.form['location']

    try:
        locIndex = __location.index(loc)
    except:
        locIndex=-1

    # add 3 becoz locIndex doesn't take bhk, sqft, bath into account while finding index
    x[locIndex+3]=1 

    return str(round(model.predict([x])[0],2))



@app.route('/')
def home():
    return app.send_static_file('app.html')

if __name__ == '__main__':
    app.run()