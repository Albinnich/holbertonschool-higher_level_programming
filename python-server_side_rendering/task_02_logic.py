from flask import Flask, render_template
import json
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
    items = []
    try:
        if os.path.exists('items.json'):
            with open('items.json') as f:
                data = json.load(f)
                items = data.get('items', [])
    except json.JSONDecodeError:
        pass
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
