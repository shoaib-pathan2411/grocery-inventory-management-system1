# Generated by Django 4.2.3 on 2023-07-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='Discounts',
            field=models.IntegerField(),
        ),
    ]