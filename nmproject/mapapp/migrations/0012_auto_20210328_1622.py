# Generated by Django 3.1.7 on 2021-03-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0011_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]