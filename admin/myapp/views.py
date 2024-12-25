from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from djongo import models

#----------------------------------------
from pymongo import MongoClient

from .models import SampleDetails

import pprint

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

# collection_name.insert_many([medicine_1])


# med_detatils = collection_name.find({})


# [x] : 전체 데이터 출력
# [] : 이름만 출력
# [] : 이름,카테고리만출력


# [] : 버튼 하나만들고 누르면 이름만 출력
# [] : 버튼 하나만들고 누르면 이름,카테고리만 출력


def index(request):
    
    
    
    
    return HttpResponse("<h1>my home<u>Django App</u> project!</h1>")


def get_list(request):
    
    print(request.method,'-----------')    
    data = collection_name.find({"common_name": "Paracetamol"})

    for r in data:
        pprint.pprint(r)
    
    
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

def get_name_list(request):
    
    # {'_id': ObjectId('676b97af1d3b476e0b2c90f1'), 'common_name': 'Paracetamol'}
    data = collection_name.find({},{"common_name"})
    
    
#   'Paracetamol'
#   'Paracetamol'
#   'Paracetamol'
#   'Paracetamol'
    for r in data:
        pprint.pprint(r['common_name'])
    
        
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")
