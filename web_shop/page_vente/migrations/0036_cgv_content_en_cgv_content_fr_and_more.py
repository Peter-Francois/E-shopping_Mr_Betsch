# Generated by Django 5.1.2 on 2025-03-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_vente', '0035_alter_cgv_version_alter_cookiespolicy_version_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cgv',
            name='content_en',
            field=models.TextField(default='', help_text='Texte complet des CGV en anglais'),
        ),
        migrations.AddField(
            model_name='cgv',
            name='content_fr',
            field=models.TextField(default='', help_text='Texte complet des CGV en français'),
        ),
        migrations.AddField(
            model_name='cookiespolicy',
            name='content_en',
            field=models.TextField(default='', help_text='Texte complet des cookies en anglais'),
        ),
        migrations.AddField(
            model_name='cookiespolicy',
            name='content_fr',
            field=models.TextField(default='', help_text='Texte complet des cookies en français'),
        ),
        migrations.AddField(
            model_name='legalmention',
            name='content_en',
            field=models.TextField(default='', help_text='Texte complet des mentions légales en anglais'),
        ),
        migrations.AddField(
            model_name='legalmention',
            name='content_fr',
            field=models.TextField(default='', help_text='Texte complet des mentions légales en français'),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='content_en',
            field=models.TextField(default='', help_text='Texte complet de la politique de confidentialité en anglais'),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='content_fr',
            field=models.TextField(default='', help_text='Texte complet de la politique de confidentialité en français'),
        ),
    ]
