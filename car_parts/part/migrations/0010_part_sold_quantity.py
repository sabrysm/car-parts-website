# Generated by Django 5.0.2 on 2024-03-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0009_part_sold_part_sold_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='sold_quantity',
            field=models.IntegerField(default=0),
        ),
    ]