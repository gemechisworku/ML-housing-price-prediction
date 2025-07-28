from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.logger import logging

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            area=float(request.form.get('area')),
            bedrooms=int(request.form.get('bedrooms')),
            bathrooms=int(request.form.get('bathrooms')),
            stories=int(request.form.get('stories')),
            parking=int(request.form.get('parking')),
            mainroad=request.form.get('mainroad'),
            guestroom=request.form.get('guestroom'),
            basement=request.form.get('basement'),
            hotwaterheating=request.form.get('hotwaterheating'),
            airconditioning=request.form.get('airconditioning'),
            prefarea=request.form.get('prefarea'),
            furnishingstatus=request.form.get('furnishingstatus')
        )
        data_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(data_df)
        logging.info(f"Prediction results returned")

        return render_template('home.html', results=round(results[0], 2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
