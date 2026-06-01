from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})

@app.route('/user', methods=['POST'])
def user():
    data = request.json

    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    return jsonify({"message": f"Welcome {data['name']}"})

app.run(debug=True)