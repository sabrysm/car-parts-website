# Generated by Django 5.0.2 on 2024-02-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0006_alter_part_consumption_alter_part_power_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]