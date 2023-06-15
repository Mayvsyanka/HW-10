from pymongo import MongoClient


def get_mongodb():

    uri = "mongodb+srv://mayvsyanka:1111@cluster0.whgftxb.mongodb.net/hw8_first_part?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.hw8_first_part
    
    return db

get_mongodb()

