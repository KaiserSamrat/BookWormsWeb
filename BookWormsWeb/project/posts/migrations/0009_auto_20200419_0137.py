# Generated by Django 2.2.7 on 2020-04-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200418_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent'), ('Exchange', 'Exchange')], max_length=200),
        ),
    ]