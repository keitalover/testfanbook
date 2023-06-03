import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient('mongodb://test:test@ac-oowgeoe-shard-00-00.twt800w.mongodb.net:27017,ac-oowgeoe-shard-00-01.twt800w.mongodb.net:27017,ac-oowgeoe-shard-00-02.twt800w.mongodb.net:27017/?ssl=true&replicaSet=atlas-5kccjl-shard-0&authSource=admin&retryWrites=true&w=majority')

db = client.dbsparta
app = Flask(__name__) 
@app.route('/')

def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # sample_receive = request.form[]'sample_give")
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanmessages.insert_one(doc) 
    return jsonify({'msg' : 'Comment Posted!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanmessages.find({}, {'_id': False}))
    return jsonify({'messages': message_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@ac-oowgeoe-shard-00-00.twt800w.mongodb.net:27017,ac-oowgeoe-shard-00-01.twt800w.mongodb.net:27017,ac-oowgeoe-shard-00-02.twt800w.mongodb.net:27017/?ssl=true&replicaSet=atlas-5kccjl-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanmessage.find({}, {'_id': False}))
    return jsonify({'message':message_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)