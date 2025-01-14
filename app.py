from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

# Chiave API NASA
NASA_API_KEY = 'VxYup1QihuUTeig45fsgYdznsIrVcade44hhe2Yq'

# Route per la home
@app.route('/')
def home():
    return render_template('home.html')

# Route per l'API NASA APOD
@app.route('/nasa')
def nasa():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template('nasa.html', apod=data)
    else:
        return f"Errore nell'accesso all'API NASA: {response.status_code}"

# Route per l'API CatFact
@app.route('/cat_fact')
def cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template('cat_fact.html', fact=data)
    else:
        return f"Errore nell'accesso all'API CatFact: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
