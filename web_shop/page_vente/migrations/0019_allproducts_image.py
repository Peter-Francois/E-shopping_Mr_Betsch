# Generated by Django 5.1.2 on 2025-02-21 09:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_vente', '0018_rename_section_id_cart_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproducts',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='image', max_length=255, null=True),
        ),
    ]
