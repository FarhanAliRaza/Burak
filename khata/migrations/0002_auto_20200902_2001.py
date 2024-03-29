# Generated by Django 2.2.7 on 2020-09-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='get',
            name='unique_id',
            field=models.CharField(default='kaka', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='give',
            name='unique_id',
            field=models.CharField(default='kaka', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='khata',
            name='unique_id',
            field=models.CharField(default='kaka', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='get',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='give',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='khata',
            name='get',
            field=models.ManyToManyField(blank=True, to='khata.Get'),
        ),
        migrations.AlterField(
            model_name='khata',
            name='give',
            field=models.ManyToManyField(blank=True, to='khata.Give'),
        ),
    ]
