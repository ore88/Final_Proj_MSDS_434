#!/usr/bin/env python
import os

from typing import Dict

from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['POST'])
def prediction(project: '571997275877', endpoint_id: '5947891713337982976', instance_dict: Dict, 
                location: str = "us-central1", api_endpoint: str = "us-central1-aiplatform.googleapis.com"):
    
    client_options = {"api_endpoint": api_endpoint}
        
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
        
    instance = json_format.ParseDict(instance_dict, Value())

    instances = [instance]

    parameters_dict = {}

    parameters = json_format.ParseDict(parameters_dict, Value())

    endpoint = client.endpoint_path(project=project, location=location, endpoint=endpoint_id)

    response = client.predict(endpoint=endpoint, instances=instances, parameters=parameters)
    
    print("response")

    print(" deployed_model_id:", response.deployed_model_id)

    # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification_1.0.0.yaml for the format of the predictions.
    
    predictions = response.predictions
    for prediction in predictions:
        print(" prediction:", dict(prediction))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))