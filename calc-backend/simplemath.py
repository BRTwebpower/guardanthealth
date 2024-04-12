from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})
api = Api(app)

#app.config['CORS_HEADERS'] = 'Content-Type'

# method for verifying api params
# @params data: array with api inputs
# @params functionName: string
# returns number status code
def checkPosted(data, functionName):
    if (functionName in ("add", "sub")):
        if "x" not in data or "y" not in data:
            return 301
        if (not isinstance(data["x"], int) or not isinstance(data["y"], int)
         or not checkNumber(data["x"]) or not checkNumber(data["y"])):
            return 305
        else:
            return 200

# method for verifying api param using ajax
# @params num: number
# return boolean
def checkNumber(num):
    pattern = r"/^[\d|\.|\,]+/"
    if re.match(pattern, str(num)):
        return False
    else:
        return True

# End point method for performing addition of two number inputs
# @params add: string
# @params methos: array get or post
# return json result
@app.route('/add', methods=['GET', 'POST'])
def add():
    data = request.get_json()
    # print(f"from add line 35 {data['x']}-{data['y']}")
    # validate posted data
    status_code = checkPosted(data, "add")
    
    if (status_code == 301):
        mapping = {
            'message': "Error: One or more parameters are missing",
            'status_code': status_code
        }
        return jsonify(mapping)
    if (status_code == 305):
        mapping = {
            'message': "Error: All parameter should be only integers",
            'status_code': status_code
        }
        return jsonify(mapping)
        
    x = data["x"]
    y = data["y"]
    x = int(x)
    y = int(y)
    # result
    res = x+y
    mapping = {
            'res': res,
            'status_code': 200
        }
    return jsonify(mapping)
    return res

# End point method for performing subtracting of two number inputs
# @params sub: string
# @params methos: array get or post
# return json result
@app.route('/sub', methods=['GET', 'POST'])
def sub():
    data = request.get_json()
    # print(f"from add line 68 {data['x']}-{data['y']}")
    # validate posted data
    status_code = checkPosted(data, "sub")
    
    if (status_code == 301):
        mapping = {
            'message': "Error: One or more parameters are missing",
            'status_code': status_code
        }
        return jsonify(mapping)
    if (status_code == 305):
        mapping = {
            'message': "Error: All parameter should be only integers",
            'status_code': status_code
        }
        return jsonify(mapping)
    
    x = data["x"]
    y = data["y"]
    x = int(x)
    y = int(y)
    # result
    res = x-y
    mapping = {
            'res': res,
            'status_code': 200
        }
    return jsonify(mapping)
    return res