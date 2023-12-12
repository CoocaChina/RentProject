
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.http import HttpResponse

from user_massage.models import Landlord
# Create your views here.

class LandlordModelForm(ModelForm):
    class Meta:
        model = Landlord
        fields = "__all__"

def index(request):
    
    if request.method =="POST":
        form= LandlordModelForm()
        tel= request.POST.get("tel")
        password= request.POST.get("password")
        land_lord=Landlord.objects.filter(landlord_phone=tel, password=password).first()
        if land_lord:
            h_name=land_lord.house_number
            return render(request,'rentPc/index/index.html',{"name":h_name})

        return render(request,'rentPc/index/login.html',{"msg":"手机号/密码错误","form":form})

    return HttpResponse("请先登录~")

def login(request):

    form= LandlordModelForm()
    if request.method =="GET":
        return render(request, 'rentPc/index/login.html',{"form":form})
    form= LandlordModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return render(request,'rentPc/index/login.html',{"msg_t":"注册成功!","form":form})
    else:
        return render(request, 'rentPc/index/login.html', {"msg_t": "注册信息错误!", "form": form})
    return render(request, 'rentPc/index/login.html',{"form":form})
    