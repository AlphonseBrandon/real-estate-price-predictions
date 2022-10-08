from flask import Flask, request, jsonify
import util # util.py

# create the Flask app

app = Flask(__name__)

# get location data from the client
@app.route('/get_location_names')

def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

# get estimated price from the client
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })

if __name__ == '__main__':
    print('Starting python Flask server for House Price Prediction')
    app.run(debug=True, host='localhost', port=5000)
