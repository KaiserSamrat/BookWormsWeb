# Generated by Django 2.2.7 on 2020-04-11 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookworms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
