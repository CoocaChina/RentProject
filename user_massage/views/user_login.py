from django.shortcuts import render,HttpResponse
from user_massage.models import User

# Create your views here.

user_msg=[]


def login(request):

    if request.method =="POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        msg = User.objects.filter(tel=phone,room_num=password[:-3])
        print(msg)
        if msg:
            user_msg.append(phone)
            user_msg.append(password[:-3])
            return render(request,"Client/index.html",{"room_num":password[:-3]})
        return render(request,"Client/login.html",{"msg":"手机号/密码错误，请重试！！"})
    return render(request,"Client/login.html")


def index(request):

    return render(request,"Client/index.html")