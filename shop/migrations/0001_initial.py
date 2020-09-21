# Generated by Django 2.2.7 on 2020-04-15 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_sub_category', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path)),
                ('name', models.CharField(max_length=255)),
                ('main_category', models.CharField(choices=[('Shop', 'Shop'), ('Manufacturer', 'Manufacturer'), ('Service', 'Service')], default='sh', max_length=2)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.ShopSubCategory')),
            ],
        ),
    ]
