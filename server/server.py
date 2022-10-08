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

if __name__ == '__main__':
    print('Starting python Flask server for House Price Prediction')
    app.run(debug=True, host='localhost', port=5000)
