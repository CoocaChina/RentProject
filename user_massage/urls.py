#后台管理子路由
from django.urls import path, include
from user_massage.views import user_login

urlpatterns = [
    #登录页
    path('user/login/', user_login.login),
    #首页
    path('user/index/', user_login.index),
    #个人信息页
    path('user/msg/', user_login.msg),
    #房租详情
    path('user/details/', user_login.details),
   #水电度数   
    path('user/hydropower/', user_login.hydropower),
    #交租历史
    path('user/history/', user_login.history),
  
]