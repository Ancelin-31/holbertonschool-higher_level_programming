#!/usr/bin/env python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_file = 'items.json'
    try:
        with open(items_file, 'r', encoding='utf-8') as i:
            data = json.load(i)
            items_array = data['items']
        return render_template('items.html', list=items_array)

    except Exception as e:
        return ("error : {}".format(e))
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)