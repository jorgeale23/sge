# Generated by Django 3.2.4 on 2021-08-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_electrodomestico_consumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajustes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Habitantes', models.PositiveIntegerField()),
                ('Politica', models.PositiveIntegerField()),
                ('Consumo', models.FloatField()),
                ('Emisferio', models.CharField(max_length=1)),
            ],
        ),
    ]