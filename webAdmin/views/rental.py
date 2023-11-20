import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.forms import ModelForm
from user_massage.models import Money,Room


class MoneyModelForm(ModelForm):
    class Meta:
        model = Money
        fields = ["id","house_number","room_num","rent_time","water_content","kwh","other",]
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        #name: 列表中字段名字可以根据name判断添加与否，field：列表中字段的对象room_price <django.forms.fields.DecimalField object at 0x00000201CC5BFF10>
        for name,field in self.fields.items():
            field.widget.attrs={"class":"form-control"}

def add(request):
    if request.method =="GET":
        form= MoneyModelForm()
        return render(request,'rentPc/rental/add.html',{"form":form})

    house_number=request.POST.get("house_number")
    room_num=request.POST.get("room_num")
    water_content=request.POST.get("water_content")
    kwh=request.POST.get("kwh")
    other=request.POST.get("other")
    old_m = Money.objects.filter(house_number=house_number,room_num=room_num).reverse()
    new_w = float(water_content)-float(old_m.first().water_content)
    new_k = float(kwh)-float (old_m.first().kwh)
    utility_bills=Room.objects.filter(house_number=house_number,room_num=room_num).first()
    ww = int(utility_bills.water_price)*new_w
    kk =int(utility_bills.power_price)*new_k
    rr= int(utility_bills.room_price)
    oo = int(other)

    form= MoneyModelForm(data= request.POST)

    if form.is_valid():
        f=form.save(commit=False)
        f.water_content=ww
        f.kwh = kk
        f.room_price = rr
        f.total = ww+kk+rr+oo
        f.save()
        return redirect("/rental/index/")
    return render(request,'rentPc/rental/add.html',{"form":form,"water_price":utility_bills.water_price,
    "power_price":utility_bills.power_price})


def index(request):
    contact_list= Money.objects.all()
    paginator = Paginator(contact_list, 20)
    # 用户点击的当前页
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'rentPc/rental/index.html',{"page_obj": page_obj})

  


def del_msg(request,nid):
    room_msg =Money.objects.filter(id=nid).delete()
    return redirect("/rental/index/")
    
    # house_number=request.POST.get("house_number")
    # room_num=request.POST.get("room_num")
    # water_content=request.POST.get("water_content")
    # kwh=request.POST.get("kwh")
    # other=request.POST.get("other")

    # old_m = Money.objects.filter(house_number=house_number,room_num=room_num).reverse()

    # new_w = float(water_content)-float(old_m.first().water_content)
    # new_k = float(kwh)-float (old_m.first().kwh)

    # utility_bills=Room.objects.filter(house_number=house_number,room_num=room_num).first()
    # ww = int(utility_bills.water_price)*new_w
    # kk =int(utility_bills.power_price)*new_k
    # rr= int(utility_bills.room_price)
    # oo = float(other)

    # print (float(water_content),float(old_m.first().water_content),float(kwh),float (old_m.first().kwh))

    # form= MoneyModelForm(data= request.POST,instance=room_msg)
    # if form.is_valid():
    #     f=form.save(commit=False)
    #     f.water_content=ww
    #     f.kwh = kk
    #     f.room_price = rr
    #     f.total = ww+kk+rr+oo
    #     f.save()
    #     return redirect("/rental/index/")
    # return render(request, 'rentPc/rental/add.html',{"form":form})