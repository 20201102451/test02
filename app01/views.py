from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("这是首页")
def index2(request):
    return HttpResponse("这是测试首页")