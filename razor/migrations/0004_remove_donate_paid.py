# Generated by Django 3.2.8 on 2021-10-24 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('razor', '0003_auto_20211022_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='paid',
        ),
    ]
