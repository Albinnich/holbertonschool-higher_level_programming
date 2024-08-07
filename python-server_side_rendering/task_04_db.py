from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM products')
    products = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in products]

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
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items=data['items'])

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        try:
            products = read_sql()
        except sqlite3.Error as e:
            error = f"Database error: {e}"
            products = []
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        product_id = int(product_id)
        products = [product for product in products if product['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
