import requests
from django.forms import ModelForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from user_massage.models import User
# Create your views here.

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ["house_number","room_num","name","gender","age","tel",
        "id_card","job","address","check_in_time","leave_time"]
        # 手动添加样式
        # widgets={
        #     "house_number":forms.TextInput(attrs={"class":"form-control"})
        # }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        #name: 列表中字段名字可以根据name判断添加与否，field：列表中字段的对象room_price <django.forms.fields.DecimalField object at 0x00000201CC5BFF10>
        for name,field in self.fields.items():
            field.widget.attrs={"class":"form-control"}




def userlist(request):
    contact_list = User.objects.all()
   
    # 执行分页
    paginator = Paginator(contact_list, 20)  # 按照5条数据一分页
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    return render(request,'rentPc/rentuser/userlist.html',{"page_obj": page_obj})

def add(request):
    if request.method =="GET":
        form= UserModelForm()
        return render(request, 'rentPc/rentuser/add.html',{"form":form})

    form= UserModelForm(data= request.POST)
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/rent/userlist/")
    return render(request, 'rentPc/rentuser/add.html',{"form":form})
   
def edit(request,name,tel):
    user_msg =User.objects.filter(house_number=name,tel=tel).first()
    if request.method=="GET":
        form= UserModelForm(instance=user_msg)
        return render(request,'rentPc/rentuser/edit.html',{"form":form})
    form= UserModelForm(data= request.POST,instance=user_msg)
    if form.is_valid():
        form.save()
        return redirect("/rent/userlist/")
    return render(request, 'rentPc/rentuser/add.html',{"form":form})