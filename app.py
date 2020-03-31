from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app)

products = [
    {
        'id': 0,
        'title': 'Apples',
        'price': 1.20
    },
    {
        'id': 1,
        'title': 'Bananas',
        'price': 1.45
    },
    {
        'id': 2,
        'title': 'Grapes',
        'price': 5.12
    },
    {
        'id': 3,
        'title': 'Blackberries',
        'price': 2.52
    },
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',title="Products", products=products)

@app.route('/api/products/all', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['GET'])
def get_products_byid():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Please specify a product id."

    results=[]    

    for product in products:
        if product['id'] == id:
            results.append(product)

    return jsonify(results)

if __name__ == '__main__':
    port= os.environ.get('PORT')
    app.run(host='0.0.0.0', debug=False, port=port)