from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("这是首页")
<<<<<<< HEAD

def index3(request):
    return HttpResponse("这是SSL首页")
=======
def index2(request):
    return HttpResponse("这是测试首页")
>>>>>>> origin/master

def indexFan(request):
    return HttpResponse("这是提交一")


def indexSSL(request):
    return HttpResponse("这是SSL提交")
