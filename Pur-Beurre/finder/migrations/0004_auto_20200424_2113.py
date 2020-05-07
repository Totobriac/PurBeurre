# Generated by Django 3.0.5 on 2020-04-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_auto_20200420_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fat',
            field=models.FloatField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='real_name',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='salt',
            field=models.FloatField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='satured_fat',
            field=models.FloatField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sugars',
            field=models.FloatField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]