"""
@author: Sourabh Sinha
This File loads the trained RandomForest model on Iris dataset
and exposes as POST API 
"""

import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger 

with open("iris_rf.pkl", "rb") as model_file:
    model = pickle.load(model_file)
    
app = Flask(__name__)
Swagger = Swagger(app)

@app.route("/predict")
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
        - name: s_len
          in: query
          type: number
          required: true
        - name: s_wdt
          in: query
          type: number
          required: true
        - name: p_len
          in: query
          type: number
          required: true  
        - name: p_wdt
          in: query
          type: number
          required: true
    responses:
          200:
              description: "0: Iris-setosa, 1: Iris-versicolor, 2: Iris-virginica"
    """
    s_len = request.args.get("s_len")
    s_wdt = request.args.get("s_wdt")
    p_len = request.args.get("p_len")
    p_wdt = request.args.get("p_wdt")

    prediction = model.predict(np.array([[s_len, s_wdt, p_len, p_wdt]]))

    return str(prediction)

@app.route("/predict_file", methods=["POST"])
def predict_iris_file():
    """Example endpoint returning a prediction of a iris file
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    responses:
          200:
              description: "0: Iris-setosa, 1: Iris-versicolor, 2: Iris-virginica"
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)