# Generated by Django 3.0.5 on 2020-04-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('picture', models.URLField()),
                ('categories', models.TextField(max_length=5000)),
            ],
        ),
    ]
