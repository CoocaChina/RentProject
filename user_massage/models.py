
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Landlord(models.Model):
    landlord_phone = models.IntegerField()
    house_number = models.CharField(max_length=255, blank=True, null=True)
    landlord_name = models.CharField(db_column='Landlord_name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'landlord'


class Money(models.Model):
    id = models.IntegerField(primary_key=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    home_id = models.IntegerField()
    rent_time = models.DateTimeField()
    water_content = models.FloatField()
    kwh = models.FloatField()
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    other = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'money'


class Room(models.Model):
    house_number = models.CharField(max_length=255, blank=True, null=True)
    water_price = models.DecimalField(max_digits=10, decimal_places=2)
    power_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_price = models.IntegerField()
    deposit = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'room'


class User(models.Model):
    house_number = models.CharField(max_length=255, blank=True, null=True)
    room_num = models.IntegerField()
    name = models.CharField(max_length=16)
    gender = models.SmallIntegerField()
    tel = models.IntegerField()
    id_card = models.BigIntegerField()
    job = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    check_in_time = models.DateTimeField(db_column='check-in_time')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'user'
