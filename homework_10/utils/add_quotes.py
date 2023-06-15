import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://mayvsyanka:1111@cluster0.whgftxb.mongodb.net/hw8_first_part?retryWrites=true&w=majority")

db = client.hw8_first_part

with open('homework_10/utils/quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({'quote': quote['quote'], 'tags': quote['tags'], 'author': ObjectId(author['_id'])})