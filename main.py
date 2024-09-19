from flask import Flask, request, jsonify, Response
app = Flask(__name__)

@app.post('/')
def home():
    data = request.get_json()
    return data

app.run(debug=True, port=5738)