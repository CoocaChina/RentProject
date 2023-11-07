#后台管理子路由
from django.urls import path, include
from user_massage.views import user_login


urlpatterns = [
    #首页
    path('user/login/', user_login.login),

]