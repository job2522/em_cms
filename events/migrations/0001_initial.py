# Generated by Django 2.1.1 on 2018-11-08 13:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_Name', models.CharField(default=None, max_length=20)),
                ('Parent_ID', models.IntegerField(max_length=4, null=True)),
                ('Cat_Level', models.IntegerField(max_length=4, null=True)),
                ('Active', models.BooleanField(default=True)),
                ('Create_date', models.DateTimeField(default=datetime.datetime(2018, 11, 8, 20, 13, 25, 403790), verbose_name='Create Date')),
                ('updated_date', models.DateTimeField(default=datetime.datetime(2018, 11, 8, 20, 13, 25, 403790), verbose_name='Update Date')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserXXX', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_pic', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shop_ID', models.IntegerField(default=1)),
                ('Shop_Name', models.CharField(max_length=200)),
                ('Shop_ShortName_TH', models.CharField(max_length=200, null=True)),
                ('Shop_ShortName_EN', models.CharField(max_length=200, null=True)),
                ('Shop_Detail_TH', models.CharField(max_length=200, null=True)),
                ('Shop_Detail_EN', models.CharField(max_length=200, null=True)),
                ('Cat_ID', models.CharField(choices=[('1', '1'), ('2', '2')], default=None, max_length=10)),
                ('Active', models.CharField(default=None, max_length=100)),
                ('icon', models.ImageField(default=None, upload_to='')),
                ('cover', models.ImageField(default=None, upload_to='')),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Floor', models.CharField(choices=[('EMP', (('Floo1', 'Floo1'), ('M', 'M'))), ('EMQ', (('G', 'G'), ('Floo1', 'Floo1'), ('M', 'M')))], default=None, max_length=10)),
                ('Tel', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128)),
                ('Branch_Code', models.CharField(choices=[('EMP', 'EMP'), ('EMQ', 'EMQ')], default=None, max_length=4)),
                ('pivot_icon', models.ImageField(null=True, upload_to='')),
                ('x_pivot', models.FloatField(default=0)),
                ('y_pivot', models.FloatField(default=0)),
                ('Create_date', models.DateTimeField(default=None, verbose_name='create date')),
                ('Create_by', models.CharField(max_length=200)),
                ('Updated_date', models.DateTimeField(default=None, verbose_name='update date')),
                ('Updated_by', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='events.Category')),
            ],
        ),
    ]
