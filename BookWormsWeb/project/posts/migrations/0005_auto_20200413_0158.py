# Generated by Django 2.2.7 on 2020-04-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
