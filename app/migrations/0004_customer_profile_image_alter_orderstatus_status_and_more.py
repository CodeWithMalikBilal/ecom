# Generated by Django 5.0.4 on 2024-07-06 10:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_customer_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profileimg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(choices=[('A', 'Accepted'), ('P', 'Packed'), ('R', 'Getting Ready'), ('DI', 'Delivered'), ('C', 'Canceled'), ('D', 'Dispached')], default='Pending', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Icecream'), ('P', 'Pizza'), ('CC', 'CupCake'), ('B', 'Burger')], max_length=2),
        ),
    ]
