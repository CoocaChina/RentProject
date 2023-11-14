from django.shortcuts import render,HttpResponse
from user_massage.models import User,Landlord,Room,Money

# Create your views here.
# 0: 用户手机号，1：房间号，2：房东手机号，3：门牌号
user_msg=[]
#用户登录
def login(request):
    user_msg.clear()
    if request.method =="POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        msg = User.objects.filter(tel=phone,room_num=password[:-3])       
        print(msg)
        if msg:
            for obj in msg:
                h_n = obj.house_number
                fangd = Landlord.objects.filter(house_number=h_n)
            for tel in fangd:
                fd_tel=tel.landlord_phone
                fh=tel.house_number
            user_msg.append(phone)
            user_msg.append(password[:-3])
            user_msg.append(fd_tel)
            user_msg.append(fh)
            return render(request,"Client/index.html",{"room_num":password[:-3],"tel":fd_tel},)
        return render(request,"Client/login.html",{"msg":"手机号/密码错误，请重试！！"})
    return render(request,"Client/login.html")

# 用户首页
def index(request):
    if user_msg:
        return render(request,"Client/index.html",{"room_num":user_msg[1],"tel":user_msg[2]},)
    return HttpResponse("用户请登录")
# 用户信息
def msg(request):

    room_mag = User.objects.filter(room_num=user_msg[1])

    return render(request,"Client/msg.html",{"room_num":user_msg[1],"tel":user_msg[2],"user_room":room_mag,})
# 租房详情

def details(request):

    room_m = Room.objects.filter(room_num=user_msg[1],house_number=user_msg[3])

    return render(request,"Client/details.html",{"room_num":user_msg[1],"tel":user_msg[2],"room_m":room_m,})
#水电度数 
def hydropower(request):

    money_m = Money.objects.filter(room_num=user_msg[1],house_number=user_msg[3])

    return render(request,"Client/hydropower.html",{"room_num":user_msg[1],"tel":user_msg[2],"money_m":money_m,})
#交租历史
def history(request):
   
    money_m = Money.objects.filter(room_num=user_msg[1],house_number=user_msg[3])

    return render(request,"Client/history.html",{"room_num":user_msg[1],"tel":user_msg[2],
    "money_m":money_m,})

