#后台管理子路由
from django.urls import path, include
from webAdmin.views import index,rent,room,rental


urlpatterns = [
    #首页

    path('', index.index, name="pc_index"),
    path('login/', index.login, name="pc_login"),
    #租客管理
    path('rent/userlist/', rent.userlist, name="rent_user_list"),

    path('rent/<str:name>/<int:tel>/edit/', rent.edit, name="rent_user_edit"),

    path('rent/add/', rent.add, name="rent_user_add"),

    #房屋管理
    path('room/index/', room.index, name="rent_room_index"),

    path('room/<str:name>/<int:rid>/edit/', room.edit, name="rent_room_edit"),

    path("room/add/",room.add,name='rent_room_add'),

    #租金管理

    path('rental/index/', rental.index, name="rental_index"),

    path("rental/add/",rental.add,name='rental_add'),

    path('rental/<int:nid>/del/', rental.del_msg, name="rent_rental_del"),

]