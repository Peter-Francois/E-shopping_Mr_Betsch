# Generated by Django 5.1.2 on 2025-02-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_vente', '0009_rename_lien_image_macrame_lien_image1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='macrame',
            name='disponible',
            field=models.BooleanField(default=False),
        ),
    ]
