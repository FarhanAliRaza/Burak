# Generated by Django 2.2.7 on 2020-09-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata', '0006_auto_20200902_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khata',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
