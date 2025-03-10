# Generated by Django 5.1.2 on 2024-10-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_vente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('ornement', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Together',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('ornement', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name='bijoux',
        ),
        migrations.AddField(
            model_name='maroquinerie',
            name='prix',
            field=models.FloatField(default=0.0),
        ),
    ]
