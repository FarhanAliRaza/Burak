# Generated by Django 2.2.7 on 2020-09-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200728_2329'),
        ('cart', '0002_cartproduct_timestamp'),
        ('order', '0007_auto_20200825_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False)),
                ('order_id', models.CharField(blank=True, max_length=20, null=True)),
                ('total', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('cart', models.ManyToManyField(to='cart.CartProduct')),
                ('wholeseller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.WholeSeller')),
            ],
        ),
    ]