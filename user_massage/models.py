
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Landlord(models.Model):
    landlord_phone = models.CharField(max_length=13,verbose_name='房东手机号')
    house_number = models.CharField(max_length=255, verbose_name='门牌号')
    landlord_name = models.CharField(db_column='Landlord_name', max_length=255, verbose_name='房东姓名')  # Field name made lowercase.
    password = models.CharField(max_length=8, verbose_name='登录密码')

    class Meta:
        managed = True
        db_table = 'landlord'


class Money(models.Model):
    house_number = models.CharField(max_length=255, verbose_name='门牌号')
    room_num = models.CharField(max_length=5,verbose_name='房间号')
    rent_time = models.DateField(verbose_name='出租时间')
    water_content = models.FloatField(verbose_name='当前用水量')
    kwh = models.FloatField(verbose_name='当前用电量')
    room_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='租金')
    other = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='其他')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='总计')

    class Meta:
        managed = True
        db_table = 'money'


class Room(models.Model):
    house_number = models.CharField(max_length=255, verbose_name='门牌号')
    water_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='电费')
    power_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='水费')
    room_price = models.CharField(max_length=11,verbose_name='租金')
    deposit = models.CharField(max_length=11,verbose_name='押金')
    room_num = models.CharField(max_length=255,verbose_name='房间号')

    class Meta:
        managed = True
        db_table = 'room'


class User(models.Model):
    house_number = models.CharField(max_length=255,verbose_name='门牌号')
    room_num = models.CharField(max_length=5,verbose_name='房间号')
    name = models.CharField(max_length=16, verbose_name='用户姓名')
    gender = models.CharField(max_length=6, verbose_name='性别')
    age = models.CharField(max_length=6, verbose_name='年龄')
    tel = models.CharField(max_length=13,verbose_name='手机号')
    id_card = models.BigIntegerField(verbose_name='身份证')
    job = models.CharField(max_length=255, verbose_name='工作')
    address = models.CharField(max_length=255,verbose_name='地址')
    check_in_time = models.DateTimeField(db_column='check-in_time', verbose_name='入住时间')  # Field renamed to remove unsuitable characters.
    leave_time = models.DateField(blank=True, null=True, verbose_name='退租时间')

    class Meta:
        managed = True
        db_table = 'user'
