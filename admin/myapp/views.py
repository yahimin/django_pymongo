from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from djongo import models


def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

from pymongo import MongoClient
from django.conf import settings
my_client = MongoClient('localhost', 27017)

#  first define the database name
dbname = my_client['sample_medicines']

# create collection name
collection_name = dbname['medicinedetails']


medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name" : "Paracetamol",
    "scientific_name" : "",
    "available" : "Y",
    "category": "fever"
}

collection_name.insert_many([medicine_1])


med_detatils = collection_name.find({})


for r in med_detatils:
    print(r['common_name'])
