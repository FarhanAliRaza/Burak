# Generated by Django 2.2.7 on 2020-09-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
