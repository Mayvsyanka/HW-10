import certifi
from mongoengine import connect



ca = certifi.where()
connection = connect(host="mongodb+srv://mayvsyanka:1111@cluster0.whgftxb.mongodb.net/hw8_first_part?retryWrites=true&w=majority",
            tlsCAFile=ca)







