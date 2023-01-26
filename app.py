from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    if id < 5000:
        data = True
    else:
        data = False

    return jsonify({'result':data})


@app.route('/id', methods=['POST'])
def post():
    dic = request.get_json()
    v_lst = list(dic.values())

    return jsonify({'name':v_lst[0]})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)