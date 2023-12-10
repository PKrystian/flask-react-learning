from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import params

App = Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI'] = params.DATABASE_URI
App.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(App)

# How to: create a table in the database
# type flask shell, then:
# 'db.create_all()'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(
        self,
        title: str,
        body: str
    ) -> None:
        self.title = title
        self.body = body
        

@App.route('/get', methods=['GET'])
def get():
    return jsonify({'method': 'GET'})

if __name__ == '__main__':
    App.run(debug=params.SERVER_DEBUG)