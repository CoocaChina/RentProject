from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Money(models.Model):
    house_number = models.CharField(max_length=255,verbose_name="门牌号")
    home_id = models.IntegerField(primary_key=True,verbose_name="房间号")
    rent_time = models.DateTimeField(verbose_name="出租时间")
    water_content = models.FloatField(verbose_name="当前用水量")
    kwh = models.FloatField(verbose_name="当前用电量")
    room_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="租金")
    other = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="其他")
    total = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="总计")

    class Meta:
        managed = True
        db_table = 'money'


class Room(models.Model):
    house_number = models.CharField(max_length=255,verbose_name="门牌号")
    home_num = models.IntegerField(verbose_name="房间号")
    water_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="水费")
    power_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="电费")
    room_price = models.IntegerField(verbose_name="租金")
    deposit = models.IntegerField(verbose_name="押金")

    class Meta:
        managed = True
        db_table = 'room'


class User(models.Model):
    house_number = models.CharField(max_length=255,verbose_name="门牌号")
    home_id = models.IntegerField(verbose_name="房间号")

    name = models.CharField(max_length=16,verbose_name="用户姓名",)
    gender_choices={
        (1,"男"),(2,"女")
    }
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)
    tel = models.IntegerField(verbose_name="手机号")
    id_card = models.BigIntegerField(verbose_name="身份证")
    job = models.CharField(max_length=255,verbose_name="工作")
    address = models.CharField(max_length=255,verbose_name="地址")
    check_in_time = models.DateTimeField(db_column='check-in_time',verbose_name="入住时间") 

    class Meta:
        managed = True
        db_table = 'user'

class Landlord(models.Model):
    Landlord_name =  models.CharField(max_length=16,verbose_name="房东姓名")
    Landlord_phone = models.IntegerField(verbose_name="房东手机号")
    house_number = models.CharField(max_length=255,verbose_name="门牌号")
    class Meta:
        managed = True
        db_table = 'landlord'
        

    
