#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import os


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
            items_array = data.get("items")
        return render_template('items.html', list=items_array)

    except Exception as e:
        return ("error : {}".format(e))

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        if product_id:
            try:
                with open('products.json', 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())['products']
                    print(data)
                    for item in data:
                        if item['id'] == product_id:
                            return render_template('product_display.html', products=item)
                        else:
                            raise IndexError('Product not found')
            except Exception as e:
                return ('Error: {}'.format(e))
        else:
            try:
                with open('products.json', 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    print(data)
                    return render_template('product_display.html', products=data['products'])
            except Exception as e:
                return 'Error: {}'.format(e)
    elif source == 'csv':
        if product_id:
            try:
                with open('products.csv', encoding='utf-8') as f:
                    data = csv.DictReader(f)
                    products_list = []
                    for item in data:
                        if item['id'] == product_id:
                            products_list.append(item)
                            print(products_list)
                            return render_template('product_display.html', products=products_list)
                        else:
                            raise IndexError('Product not found')
            except Exception as e:
                return 'Error: {}'.format(e)
        else:
            try:
                with open('products.csv', 'r', encoding='utf-8') as f:
                    data = csv.DictReader(f)
                    products_list = []
                    for item in data:
                        products_list.append(item)
                    return render_template('product_display.html', products=products_list)
            except Exception as e:
                return 'Error: {}'.format(e)
    else:
        return ('Error: No source found')

if __name__ == '__main__':
    app.run(debug=True, port=5000)