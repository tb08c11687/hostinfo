# Generated by Django 2.1.3 on 2018-12-02 12:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_user', models.CharField(max_length=8)),
                ('host', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('[ABC]-\\d{1}-\\d{4}$', message='格式错误，示例：B-1-0195')])),
                ('displayer', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('[ABC]-\\d{1}-\\d{4}$', message='格式错误，示例：B-1-0195')])),
                ('mem', models.CharField(max_length=2)),
                ('cpu', models.CharField(max_length=16)),
                ('ip_addr', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('\\d{2,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message='格式错误，示例：192.168.24.30')])),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Department')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=8)),
                ('password', models.CharField(default='Mirror-0', max_length=20)),
            ],
        ),
    ]
