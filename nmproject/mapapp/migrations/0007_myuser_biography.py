# Generated by Django 3.1.7 on 2021-03-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0006_remove_myuser_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='biography',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
