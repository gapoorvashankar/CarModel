
# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pickle
import datetime as dt
import pandas as pd
import json


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

with open('model.pickle', 'rb') as f:
    mdl = pickle.load(f)

# making a class for model
class CarModel(Resource):
    
    # Corresponds to POST request
    def post(self):
        data = pd.DataFrame([request.get_json(force=True)])
        pred=mdl.predict(data)
        out = pred.tolist()[0]
        response = app.response_class(
        response=json.dumps(out),
        mimetype='application/json'
        )
        return response
  

# adding the defined resources along with their corresponding urls
api.add_resource(CarModel, '/carmodel')
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)