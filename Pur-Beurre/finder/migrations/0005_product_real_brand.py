# Generated by Django 3.0.5 on 2020-04-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_auto_20200424_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='real_brand',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
