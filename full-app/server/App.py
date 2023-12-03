from flask import Flask, jsonify, request
import params

App = Flask(__name__)

@App.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    App.run(debug=params.SERVER_DEBUG)