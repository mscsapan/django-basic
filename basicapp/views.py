from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home/home.html',{'name':'Basic App'})

def dashboard(request):
    return render(request,'index.html')

def request_with_param(request,id):
    print(f'requested-id {type(id)}')
    # user_id = ''
    # if isinstance(id,str):
    #     user_id = id
    # elif isinstance(id,int):
    #     user_id = str(id)
    return render(request,'params.html',{'id':id})