import json
import requests
from django.core.paginator import Paginator
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse
from user_massage.models import Room 
from django.http import HttpResponse
from django import forms

class RoomModelForm(ModelForm):
    class Meta:
        model = Room
        fields = ["house_number","room_num","water_price","power_price","room_price","deposit"]
        # 手动添加样式
        # widgets={
        #     "house_number":forms.TextInput(attrs={"class":"form-control"})
        # }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        #name: 列表中字段名字可以根据name判断添加与否，field：列表中字段的对象room_price <django.forms.fields.DecimalField object at 0x00000201CC5BFF10>
        for name,field in self.fields.items():
            field.widget.attrs={"class":"form-control"}
  

def add(request):
    if request.method =="GET":
        form= RoomModelForm()
        return render(request, 'rentPc/rentroom/add.html',{"form":form})
# 校验是否为空
    form= RoomModelForm(data= request.POST)
    if form.is_valid():
        form.save()
        return redirect("/room/index/")  
    return render(request, 'rentPc/rentroom/add.html',{"form":form})
    

def edit(request,name,rid):
    room_msg =Room.objects.filter(house_number=name,room_num=rid).first()
    if request.method=="GET":
        form= RoomModelForm(instance=room_msg)
        return render(request,'rentPc/rentroom/edit.html',{"form":form})
    form= RoomModelForm(data= request.POST,instance=room_msg)
    if form.is_valid():
        form.save()
        return redirect("/room/index/")
    return render(request, 'rentPc/rentroom/add.html',{"form":form})
   
def index(request):
    contact_list= Room.objects.all()
    print(contact_list)
    paginator = Paginator(contact_list, 20)
    # 用户点击的当前页
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'rentPc/rentroom/room_list.html',{"page_obj": page_obj})