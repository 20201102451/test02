from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("这是首页")


def index3(request):
    return HttpResponse("这是SSL首页")


def index2(request):
    return HttpResponse("这是测试首页")


def indexfan(request):
    return HttpResponse("这是提交一")


def indexfan02(request):
    return HttpResponse("这是提交二")


def indexssl(request):
    return HttpResponse("这是SSL提交")
def indexZhang(request):
    return HttpResponse("这是Zhang提交")

def indexZhang2(request):
    return HttpResponse("这是Zhang2提交")
def indexLiang(request):
    return HttpResponse("这是Liang提交")

def indextestError(request):
    return HttpResponse("这是演示远程多人提交冲突！")
