from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/get', methods=['GET'])
def get():
    return "Get Request"

#mock data for testing
@app.route('/get_mock', methods=['GET'])
def get_mock(user_id):
    #create a dictionary
    mock_data = {
        "user_id": user_id,
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get('extra')
    if extra:
        mock_data['extra'] = extra
      
    #jsonify the dictionary and pass status code 
    return jsonify(mock_data), 200

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