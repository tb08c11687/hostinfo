# Generated by Django 2.1.3 on 2018-11-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20181129_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]