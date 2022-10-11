from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("这是首页")

def index3(request):
    return HttpResponse("这是SSL首页")