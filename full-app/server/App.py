from flask import Flask, jsonify, request
import params

App = Flask(__name__)

@App.route('/put', methods=['PUT'])
def put():
    return jsonify({'method': 'PUT'})
@App.route('/get', methods=['GET'])
def get():
    return jsonify({'method': 'GET'})
@App.route('/post', methods=['POST'])
def post():
    return jsonify({'method': 'POST'})
@App.route('/delete', methods=['DELETE'])
def delete():
    return jsonify({'method': 'DELETE'})
@App.route('/patch', methods=['PATCH'])
def patch():
    return jsonify({'method': 'PATCH'})
@App.route('/options', methods=['OPTIONS'])
def options():
    return jsonify({'method': 'OPTIONS'})
@App.route('/head', methods=['HEAD'])
def head():
    return jsonify({'method': 'HEAD'})
@App.route('/trace', methods=['TRACE'])
def trace():
    return jsonify({'method': 'TRACE'})
@App.route('/connect', methods=['CONNECT'])
def connect():
    return jsonify({'method': 'CONNECT'})
@App.route('/any', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE', 'CONNECT'])
def any():
    return jsonify({'method': 'ANY'})

if __name__ == '__main__':
    App.run(debug=params.SERVER_DEBUG)