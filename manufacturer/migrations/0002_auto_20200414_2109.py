# Generated by Django 2.2.7 on 2020-04-15 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturesubcategory',
            old_name='shop_sub_category',
            new_name='manufacturer_sub_category',
        ),
    ]