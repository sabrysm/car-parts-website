# Generated by Django 5.0.2 on 2024-03-11 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0012_part_quantity_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='quantity_sold',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='quantity_sold',
        ),
    ]
