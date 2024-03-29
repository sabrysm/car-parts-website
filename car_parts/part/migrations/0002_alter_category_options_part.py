# Generated by Django 5.0.2 on 2024-02-23 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('power', models.CharField(max_length=255)),
                ('consumption', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
