from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    return {"message": ""}

@app.route('/id', methods=['POST'])
def post():
    return {'name': ''}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)