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
def Error(request):
    return HttpResponse("啦啦啦")

def indextrain1(request):
    return HttpResponse("ssl第一次提交")

def indexerror2(request):
    return HttpResponse("远程多人冲突测试")
def Error3(request):
    return HttpResponse("心海我老婆")

def indexerror3(request):
    return HttpResponse("远程多人冲突测试")
def error4(request):
    return HttpResponse("远程多人冲突测试")
def error5(request):
    return HttpResponse("远程多人冲突测试")