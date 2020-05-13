from flask import Flask, request

app = Flask(__name__)

biodiesel = 0

@app.route('/biodiesel', methods=['POST'])
def postBiodiesel():
    data = request.get_json()
    global biodiesel
    var = data.get('biodiesel')
    biodiesel += var
    print(biodiesel)
    response = {
        'biodiesel': biodiesel
    }
    return response


@app.route('/biodiesel', methods=['GET'])
def getBiodisel():
    global biodiesel
    response = {
        'biodiesel': biodiesel
    }
    return response


def create_app():
    global app
    return app
