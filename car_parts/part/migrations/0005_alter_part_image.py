# Generated by Django 5.0.2 on 2024-02-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0004_remove_part_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='image',
            field=models.ImageField(blank=True, default='product_images/default_image.jpg', null=True, upload_to='product_images'),
        ),
    ]