from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import params
from flask_marshmallow import Marshmallow
from flask_cors import CORS


App = Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI'] = params.DATABASE_URI
App.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
CORS(App)

db = SQLAlchemy(App)
ma = Marshmallow(App)

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

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

@App.route('/', methods=['GET'])
def home():
    return "Welcome to my Flask app!"

@App.route('/get', methods=['GET'])
def get():
    all_articles = Article.query.all()
    result = articles_schema.dump(all_articles)
    return jsonify(result)

@App.route('/add', methods=['POST'])
def add_article():
    if request.json is not None:
        title = request.json['title']
        body = request.json['body']

        new_article = Article(title, body)
        db.session.add(new_article)
        db.session.commit()

        return article_schema.jsonify(new_article)
    else:
        return jsonify({'error': 'No JSON received'})

if __name__ == '__main__':
    App.run(debug=params.SERVER_DEBUG)