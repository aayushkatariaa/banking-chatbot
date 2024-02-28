from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "John": {"acc_no": [123, 456, 789], "balance": 1000.00},
    "Alice": {"acc_no": [321, 654, 987], "balance": 1500.00}
}

auth_code = 123456

@app.route('/greet', methods=['POST'])
def greet_user():
    return jsonify({"message": "Welcome to Banking Chatbot! How can I assist you today?"})

@app.route('/get_user', methods=['POST'])
def get_user():
    data = request.json
    name = data.get("name")
    return jsonify({"name": name})

@app.route('/get_auth_code', methods=['POST'])
def get_auth_code():
    data = request.json
    name = data.get("name")
    return jsonify({"auth_code": auth_code})

@app.route('/get_details', methods=['POST'])
def get_details():
    data = request.json
    acc_no = data.get("acc_no")
    user = users.get("John") 
    return jsonify({"name": "John", "acc_no": user["acc_no"], "balance": user["balance"]})

@app.route('/user_search', methods=['POST'])
def user_search():
    data = request.json
    name = data.get("name")
    user = users.get(name)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/transfer_money', methods=['POST'])
def transfer_money():
    data = request.json
    acc_no1 = data.get("acc_no1")
    acc_no2 = data.get("acc_no2")
    amount = data.get("amount")
    return jsonify({"success": 1}) 

if __name__ == '__main__':
    app.run(debug=True)
