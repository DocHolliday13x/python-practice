from flask import Flask, request, jsonify

app = Flask(__name__)

#global mock data variable
mock_data = {
        "user_id": 1,
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }


@app.route('/')
def home():
    return "Home Page"

@app.route('/get', methods=['GET'])
def get():
    return "Get Request"

@app.route('/get_mock', methods=['GET'])
def get_mock():
    extra = request.args.get('extra')
    if extra:
        mock_data['extra'] = extra
      
    #jsonify the dictionary and pass status code 
    return jsonify(mock_data), 200


@app.route('/post', methods=['POST'])
def post():
    return "Post Request"

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201


@app.route('/put', methods=['PUT'])
def put():
    return "Put Request"

@app.route('/put/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    
    if 'user_id' in mock_data and mock_data['user_id'] == user_id:
        mock_data['name'] = data.get('name', mock_data['name'])
        mock_data['age'] = data.get('age', mock_data['age'])
        mock_data['email'] = data.get('email', mock_data['email'])
        
        return jsonify(mock_data), 200
    else:
        return jsonify({"error": "User not found"}), 404
    

@app.route('/delete', methods=['DELETE'])
def delete():
    return "Delete Request"

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Check if the user_id exists in the mock_data dictionary
    if 'user_id' in mock_data and mock_data['user_id'] == user_id:
        # Remove the user from the mock_data dictionary
        del mock_data['user_id']
        return "User deleted successfully", 200
    else:
        return "User not found", 404


if __name__ == '__main__':
    app.run(debug=True)