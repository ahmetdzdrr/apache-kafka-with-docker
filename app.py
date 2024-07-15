from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

@app.route('/products', methods=['GET'])
def get_products():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
