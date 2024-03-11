# Generated by Django 5.0.2 on 2024-03-10 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0008_alter_part_brand_alter_part_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='part',
            name='sold_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
