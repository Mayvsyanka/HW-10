import os
import django
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'homework_10.settings')
django.setup()


########################################



import certifi
from mongoengine import connect

ca = certifi.where()
connection = connect(host="mongodb+srv://mayvsyanka:1111@cluster0.whgftxb.mongodb.net/hw8_first_part?retryWrites=true&w=majority",
                     tlsCAFile=ca)


#############


from quotes.models import Author, Tag, Quote
from mongo_models import Quote as Q, Author as A

authors = A.objects()

for author in authors:
    print(author.fullname)
    print(author.born_date)
    print(author.born_location)
    print(author.description)
    
    Author.objects.get_or_create(
        fullname=author.fullname,
        born_date=author.born_date,
        born_location=author.born_location,
        description=author.description
    )

quotes = Q.objects()
authors = A.objects()

for quot in quotes:
    tags = []
    for tag in quot['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    print(tags)