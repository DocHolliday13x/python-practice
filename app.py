from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/get', methods=['GET'])
def get():
    return "Get Request"

@app.route('/post', methods=['POST'])
def post():
    return "Post Request"

@app.route('/put', methods=['PUT'])
def put():
    return "Put Request"

@app.route('/delete', methods=['DELETE'])
def delete():
    return "Delete Request"


if __name__ == '__main__':
    app.run(debug=True)