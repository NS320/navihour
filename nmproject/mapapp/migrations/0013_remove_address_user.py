# Generated by Django 3.1.7 on 2021-03-28 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0012_auto_20210328_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]