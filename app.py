from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    data = None
    return render_template('index.html',data = data) 


@app.route('/', methods = ['POST'])
def get_weather_data():
    data = None
    city = request.form['city']
    country = request.form['country']
    if city and country:    
        weather_data = get_weather(city,country)
    
        data = {
            "weather_data" : weather_data,
            "city": city,
            "country" : country
        }
    return render_template('index.html',data = data)    

if __name__ == '__main__':
    app.run(debug = True)