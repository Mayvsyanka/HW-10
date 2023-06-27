import json
from bson.objectid import ObjectId

from pymongo import MongoClient

uri = "mongodb+srv://mayvsyanka:0953194868@mycluster.2qefzpi.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.test

with open('homework_10/utils/quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({'quote': quote['quote'], 'tags': quote['tags'], 'author': ObjectId(author['_id'])})