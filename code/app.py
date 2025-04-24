# Importing essential libraries

from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib

# Load the Random Forest CLassifier model

classifier = joblib.load('knn_cv_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            st = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])
            
            data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
            my_prediction = classifier.predict(data)
            
            return render_template('result.html', prediction=my_prediction)
        except Exception as e:
            # Handle any exceptions and return an error message
            return jsonify({'error': str(e)})
if __name__ == '__main__':
	app.run(debug=True)
'''if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)'''

