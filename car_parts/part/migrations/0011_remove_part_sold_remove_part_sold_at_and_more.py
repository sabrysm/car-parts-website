# Generated by Django 5.0.2 on 2024-03-11 09:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0010_part_sold_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='part',
            name='sold_at',
        ),
        migrations.RemoveField(
            model_name='part',
            name='sold_quantity',
        ),
        migrations.CreateModel(
            name='SaleHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.IntegerField()),
                ('sold_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part.part')),
            ],
        ),
    ]
