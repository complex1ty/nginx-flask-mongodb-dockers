import os
from flask import Flask
from pymongo import MongoClient
from random import randint

app = Flask(__name__)
username = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
password = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
client = MongoClient(
    "mongodb://mongodb:27017",
    username=username,
    password=password
)
db = client.testdb

@app.route('/test')
def hello():
    return 'Hello World!'


@app.route('/api')
def insert_mongo_db():
    rand = randint(0, 100)
    item = {'number': randint(0, 100)}
    db.test_collection.insert_one(item)
    return 'Insert ' + str(rand) + ' into MongoDB!'

@app.route('/api/get')
def get_mongo_db():
    rand = db.test_collection.find_one()['number']
    return 'Get ' + str(rand) + ' from MongoDB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)