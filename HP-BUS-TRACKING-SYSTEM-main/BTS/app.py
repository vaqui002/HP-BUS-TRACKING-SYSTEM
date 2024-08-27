from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'AIzaSyA_i892LjXn1a7Xrwl6rc7hL54CJnVqqmU'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        
        directions = get_directions(origin, destination)
        
        return render_template('index.html', directions=directions)
    
    return render_template('index.html', directions=None)

def get_directions(origin, destination):
    params = {
        'origin': origin,
        'destination': destination,
        'key': API_KEY
    }

    response = requests.get("https://maps.googleapis.com/maps/api/directions/json", params=params)
    data = response.json()

    if data['status'] == 'OK':
        route = data['routes'][0]
        steps = []
        for step in route['legs'][0]['steps']:
            steps.append(step['html_instructions'])
        distance = route['legs'][0]['distance']['text']
        duration = route['legs'][0]['duration']['text']
        return {
            'steps': steps,
            'distance': distance,
            'duration': duration
        }
    else:
        return None

if __name__ == "__main__":
    app.run(debug=True)
