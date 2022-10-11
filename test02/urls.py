"""test02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app01.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',app01.views.index),
    path('index2/',app01.views.index2),
    path('index3',app01.views.index3),
    path('index/Fan/',app01.views.indexFan),
    path('index/SSL/',app01.views.indexSSL),
    path('index/Fan/02',app01.views.indexFan02),
    path('index/Zhang/',app01.views.indexZhang),#author:Zhang
    path('index/Fan/',app01.views.indexfan),
    path('index/SSL/',app01.views.indexssl),
    path('index/Fan/02',app01.views.indexfan02),
    path('index/Zhang2/',app01.views.indexZhang2),
    path('index/testError',app01.views.indextestError),
]
