from flask import Flask, request, jsonify
app = Flask(__name__)

users = {
    "1": {"name": "Alice", "age": 30},
    "2": {"name": "Bob", "age": 25}
}

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/user/<user_id>/details', methods=['GET'])
def user_details(user_id):
    user = users.get(user_id)
    if user:
        user_detail = {"description": f"{user['name']} is {user['age']} years old."}
        return jsonify(user_detail), 200
    return jsonify({"error": "Details not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)