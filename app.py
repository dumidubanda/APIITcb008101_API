from flask import Flask, request, redirect, render_template, jsonify
from pymongo import MongoClient
from bson import json_util
import requests

app = Flask(__name__)

client = MongoClient()
db = client["APIIT"]
collection = db.to_dos

@app.route('/')
def index():
    user = {'username': 'Bandara'}
    return render_template('index.html', title='Homepage', user=user)

@app.route('/contact')
def contact():
    user = {'username': 'Bandara'}
    return render_template('contact.html', title='Homepage', user=user)

@app.route('/aboutUs')
def aboutUs():
    user = {'username': 'Bandara'}
    return render_template('aboutUs.html', title='Homepage', user=user)

@app.route('/blog')
def blog():
    user = {'username': 'Bandara'}
    return render_template('blog.html', title='Homepage', user=user)

@app.route('/concertTours')
def concertTours():
    user = {'username': 'Bandara'}
    return render_template('concertTours.html', title='Homepage', user=user)

@app.route('/elements')
def elements():
    user = {'username': 'Bandara'}
    return render_template('elements.html', title='Homepage', user=user)

@app.route('/view', methods=['GET'])
def get_todos():
    to_dos = list(collection.find())
    return json_util.dumps(to_dos)


@app.route('/search')

def search():

    recipe = request.args.get('a', 0, type=str)

    response = requests.get(f"https://searchly.asuarez.dev/api/v1/song/search?query={recipe}")

    response = response.json()["response"]["results"][0]

    return jsonify(result=response) 



@app.route('/add', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        new_todo = request.get_json()
        name = new_todo['name']
        description = new_todo['description']
        time = new_todo['time']

        collection.insert_one({
            "name": name, 
            "description": description,
            "time": time
        })
        return redirect('/view')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)

