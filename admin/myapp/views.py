from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from djongo import models

#----------------------------------------
from pymongo import MongoClient


from pprint import pprint

from django.http import JsonResponse

from .forms import UserField

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

#### CRUD Pymongo + Django
# [x] : 전체 데이터 출력
# [x] : 카타고리만 출력
# [x] : 이름,카테고리만출력


# [x] : 버튼 하나만들고 누르면 데이터 추가
# [x] : form 하나 만들고 입력하고 누르면 데이처 추가
# [] : 버튼 하나만들고 누르면 이름,카테고리만 출력

#--------------------------------------------------

# [] : nginx + djanogo


def index(request):    
    return render(request,'view.html')


def get_list(request):
    
    print(request.method,'-----------')    
    # Convert cursor to list
    # 몽고디비는 항상 리스트를 convert 해줘서 던져줘야한다
    data = list(collection_name.find({}))
    try:
        for p in data:
            pprint(p)
        return render(request,'list.html', {"data" :data})
    
    except Exception as e:
        return HttpResponse(f"<h1>{str(e)}</h1>")
    
    
    # return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

def get_name_list(request):
    
    # {'_id': ObjectId('676b97af1d3b476e0b2c90f1'), 'common_name': 'Paracetamol'}
    data = list(collection_name.find({},{"common_name"}))
    
    
#   'Paracetamol'
#   'Paracetamol'
#   'Paracetamol'
#   'Paracetamol'
    for r in data:
        pprint(r['common_name'])
    
    return render(request,"name_list.html",{'data': data})
    

def add_user(request):
    
    print(request.method)
    
    if request.method =='POST':
        
       medicine_2 ={
        "medicine_id": "RR000342522",
        'common_name' : 'Jeon',
        "availabe" : 'Y',
        "category" : 'type 2 hh'
    }
       collection_name.insert_many([medicine_2])
    
 
    
    return HttpResponse('<h1>hi</h1>')


def add_detail_user(request):
    
    if request.method == 'POST':
        form = UserField(request.POST)
        
        if form.is_valid():
            try:
                print(form.cleaned_data)
                collection_name.insert_one(form.cleaned_data)
                        
            except Exception as e:
                return HttpResponse(f"<h1>{str(e)}</h1>")           
   
    
    if request.method == 'GET':
        form = UserField()
        
    return render(request,'form.html',{'form': form})