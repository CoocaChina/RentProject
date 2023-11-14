
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
#房东表
class Landlord(models.Model):
    landlord_phone = models.CharField(max_length=13)
    house_number = models.CharField(max_length=255)
    landlord_name = models.CharField(db_column='Landlord_name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'landlord'

#金钱表
class Money(models.Model):
    id = models.IntegerField(primary_key=True)
    house_number = models.CharField(max_length=255)
    room_num = models.CharField(max_length=5)
    rent_time = models.DateTimeField()
    water_content = models.FloatField()
    kwh = models.FloatField()
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    other = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'money'

#房间表
class Room(models.Model):
    house_number = models.CharField(max_length=255)
    water_price = models.DecimalField(max_digits=10, decimal_places=2)
    power_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_price = models.CharField(max_length=11)
    deposit = models.CharField(max_length=11)
    room_num = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'room'

# 用户表
class User(models.Model):
    house_number = models.CharField(max_length=255)
    room_num = models.CharField(max_length=5)
    name = models.CharField(max_length=16)
    gender = models.SmallIntegerField()
    tel = models.CharField(max_length=13)
    id_card = models.BigIntegerField()
    job = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    check_in_time = models.DateTimeField(db_column='check-in_time')  # Field renamed to remove unsuitable characters.
    create_by = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=datetime.now)
    def toDict(self):
        return {'house_number':self.house_number,'room_num':self.room_num,'name':self.name,'gender':self.gender,'tel':self.tel,'id_card':self.id_card,'job':self.job,'address':self.address,'check_in_time':self.check_in_time.strftime('%Y-%m-%d %H:%M:%S'),'create_by':self.create_by,'create_at':self.create_by.create_at('%Y-%m-%d %H:%M:%S')}
    class Meta:
        managed = True
        db_table = 'user'
