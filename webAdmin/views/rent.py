import json

import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from user_massage.models import User

from django.http import HttpResponse
# Create your views here.

def index(request,pIndex=1):
    mmod = User.objects
    mlist = mmod.filter()
    mywhere = []
    # 获取搜索条件并判断
    kw = request.GET.get("keyword", None)
    if kw:
        mlist = mlist.filter(name__contains=kw)
        mywhere.append('keyword=' + kw)
    status = request.GET.get("status", None)
    if status:
        mlist = mlist.filter(status=status)
        mywhere.append("status=" + status)
    # 执行分页
    pIndex = int(pIndex)
    page = Paginator(mlist, 5)  # 按照5条数据一分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断页码是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码信息
    context = {"rentuserlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "rentPc/rentuser/index.html", context)

def add(request):
    return render(request, 'rentPc/rentuser/add.html')