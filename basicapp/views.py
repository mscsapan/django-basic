from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home/home.html',{'name':'Basic App'})

def dashboard(request):
    return render(request,'index.html')

def request_with_param(request,id):
    # print(f'requested-id {type(id)}')
    
    converted_id = int(id)
    
    filter_data = {}
    
    my_data = [
        {'id': 1,'name':'Mohammad','email':'mohammad@gmail.com'},
        {'id': 2,'name':'Ali','email':'ali@gmail.com'},
        {'id': 3,'name':'Khan','email':'khan@gmail.com'},
        {'id': 4,'name':'Anika','email':'anika@gmail.com'},
        {'id': 5,'name':'Taha','email':'taha@gmail.com'},
        {'id': 6,'name':'Taskeen','email':'taha.taaskeen@gmail.com'},
        {'id': 7,'name':'Ibrahim','email':'ibrahim@gmail.com'},
    ]
    
    for i in my_data:
        print(f'i is {i}')
        print(f'loop is type {type(i['id'])} - {converted_id} - {type(converted_id)}')
        
        if i['id'] == converted_id:
            filter_data = i
            break
    
    print(f'filter-data {filter_data}')
    
    # user_id = ''
    # if isinstance(id,str):
    #     user_id = id
    # elif isinstance(id,int):
    #     user_id = str(id)
    return render(request,'params.html',{'id':id,'data':filter_data})