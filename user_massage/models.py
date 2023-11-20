# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


class Landlord(models.Model):
    landlord_phone = models.CharField(verbose_name="房东手机号",max_length=13,null=True)
    house_number = models.CharField(verbose_name="出租门牌号",max_length=255,null=True)
    landlord_name = models.CharField(verbose_name="房东姓名",db_column='Landlord_name', max_length=255,null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'landlord'


class Money(models.Model):
    # id = models.IntegerField(primary_key=True)
    house_number = models.CharField(verbose_name="门牌号",max_length=255,null=True)
    room_num = models.CharField(verbose_name="房间号",max_length=5,null=True)
    rent_time = models.DateField(verbose_name="记录时间",null=True)
    water_content = models.FloatField(verbose_name="用水量",null=True)
    kwh = models.FloatField(verbose_name="用电量",null=True)
    room_price = models.DecimalField(verbose_name="房租",max_digits=10, decimal_places=2,null=True)
    other = models.DecimalField(verbose_name="其他",max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(verbose_name="总计",max_digits=10, decimal_places=2,null=True)

    class Meta:
        managed = True
        db_table = 'money'


class Room(models.Model):
    house_number = models.CharField(verbose_name="门牌号",max_length=255,null=True)
    water_price = models.DecimalField(verbose_name="水费",max_digits=10, decimal_places=2,null=True)
    power_price = models.DecimalField(verbose_name="电费",max_digits=10, decimal_places=2,null=True)
    room_price = models.CharField(verbose_name="房租",max_length=11,null=True)
    deposit = models.CharField(verbose_name="押金",max_length=11,null=True)
    room_num = models.CharField(verbose_name="房间号",max_length=255,null=True)

    class Meta:
        managed = True
        db_table = 'room'


class User(models.Model):
    house_number = models.CharField(verbose_name="门牌号",max_length=255,null=True)
    room_num = models.CharField(verbose_name="房间号",max_length=5,null=True)
    name = models.CharField(verbose_name="姓名",max_length=16,null=True)
    gender = models.CharField(verbose_name="性别",max_length=6,null=True)
    age = models.CharField(verbose_name="年龄",max_length=6,default="00")
    tel = models.CharField(verbose_name="手机号",max_length=13,null=True)
    id_card = models.BigIntegerField(verbose_name="身份证",null=True)
    job = models.CharField(verbose_name="工作",max_length=255,null=True)
    address = models.CharField(verbose_name="籍贯",max_length=255,null=True)
    check_in_time = models.DateField(verbose_name="入住时间",db_column='check-in_time')  # Field renamed to remove unsuitable characters.
    leave_time = models.DateField(verbose_name="搬离时间",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
