#后台管理子路由
from django.urls import path, include
from webAdmin.views import index,rent


urlpatterns = [
    #首页

    path('', index.index, name="pc_index"),
    path('login/', index.login, name="pc_login"),
    #租客管理
    path('rent/<int:pIndex>', rent.index, name="rent_user_index"),
    path('rent/add/', rent.add, name="rent_user_add"),
]