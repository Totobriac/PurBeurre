# Generated by Django 3.0.5 on 2020-04-29 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0008_auto_20200429_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedproduct',
            name='saved_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finder.Product'),
        ),
    ]
