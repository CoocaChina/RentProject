# Generated by Django 3.0.5 on 2023-11-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Landlord_name', models.CharField(max_length=16, verbose_name='房东姓名')),
                ('Landlord_phone', models.IntegerField(verbose_name='房东手机号')),
                ('house_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='门牌号')),
            ],
            options={
                'db_table': 'landlord',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('house_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='门牌号')),
                ('home_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='房间号')),
                ('rent_time', models.DateTimeField(verbose_name='出租时间')),
                ('water_content', models.FloatField(verbose_name='当前用水量')),
                ('kwh', models.FloatField(verbose_name='当前用电量')),
                ('room_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='租金')),
                ('other', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='其他')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总计')),
            ],
            options={
                'db_table': 'money',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='门牌号')),
                ('home_num', models.IntegerField(verbose_name='房间号')),
                ('water_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='水费')),
                ('power_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='电费')),
                ('room_price', models.IntegerField(verbose_name='租金')),
                ('deposit', models.IntegerField(verbose_name='押金')),
            ],
            options={
                'db_table': 'room',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='门牌号')),
                ('home_id', models.IntegerField(verbose_name='房间号')),
                ('name', models.CharField(max_length=16, verbose_name='用户姓名')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('tel', models.IntegerField(verbose_name='手机号')),
                ('id_card', models.BigIntegerField(verbose_name='身份证')),
                ('job', models.CharField(max_length=255, verbose_name='工作')),
                ('address', models.CharField(max_length=255, verbose_name='地址')),
                ('check_in_time', models.DateTimeField(db_column='check-in_time', verbose_name='入住时间')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
