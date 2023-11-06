#后台管理子路由
from django.urls import path, include
from webAdmin.views import index


urlpatterns = [
    #首页

    path('', index.index, name="ruhrpc_index"),

]