from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store passwords in memory
password_store = {}

@app.route('/')
def home():
    return "Welcome to the Password Manager"

@app.route('/health')
def health():
    return "App is running fine"

@app.route('/add', methods=['POST'])
def add_password():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Both username and password are required"}), 400

    username = data['username']
    password = data['password']
    password_store[username] = password

    return jsonify({"message": f"Password saved for {username}"}), 201

@app.route('/get/<username>')
def get_password(username):
    if username not in password_store:
        return jsonify({"error": "Username not found"}), 404

    return jsonify({"username": username, "password": password_store[username]})

@app.route('/delete/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in password_store:
        return jsonify({"error": "Username not found"}), 404

    del password_store[username]
    return jsonify({"message": f"User {username} deleted successfully"})


# Make sure app.run() is ONLY placed at the very end of the file
if __name__ == '__main__':
    app.run(debug=True)