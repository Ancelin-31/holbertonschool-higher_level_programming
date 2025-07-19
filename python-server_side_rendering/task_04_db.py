#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3


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
    message = None
    
    if source == 'json':
        if product_id:
            try:
                with open('products.json', 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    for item in data:
                        if item['id'] == int(product_id):
                            return render_template('product_display.html', products=[item])
                        else:
                            return render_template('product_display.html', message='Product not found')
            except Exception as e:
                return render_template('product_display.html', message=e)
        else:
            try:
                with open('products.json', 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    return render_template('product_display.html', products=data)
            except Exception as e:
                return render_template('product_display.html', message=e)
    elif source == 'csv':
        if product_id:
            try:
                with open('products.csv', encoding='utf-8') as f:
                    data = csv.DictReader(f)
                    products_list = []
                    for item in data:
                        if item['id'] == product_id:
                            products_list.append(item)
                            return render_template('product_display.html', products=products_list)
                        else:
                            return render_template('product_display.html', message='Product not found')
            except Exception as e:
                render_template('product_display.html', message=e)
        else:
            try:
                with open('products.csv', 'r', encoding='utf-8') as f:
                    data = csv.DictReader(f)
                    products_list = []
                    for item in data:
                        products_list.append(item)
                    return render_template('product_display.html', products=products_list)
            except Exception as e:
                return render_template('product_display.html', message=e)
    elif source=='sql':
        connection = sqlite3.connect('products.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name, category, price
            FROM Products
        """)
        result = cursor.fetchall()
        connection.close()
        return render_template('product_display.html', products = [dict(row) for row in result])
    else:
        return render_template('product_display.html', message='Wrong source')

if __name__ == '__main__':
    app.run(debug=True, port=5000)