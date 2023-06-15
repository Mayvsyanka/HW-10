from django.shortcuts import render

# Create your views here.
from .utils import get_mongodb

def main(request):
    db = get_mongodb()
    quotes = db.quote.find()
    return render (request, 'quotes/index.html', context={"quotes":quotes})