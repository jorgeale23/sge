# Generated by Django 3.2.4 on 2021-09-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20210824_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lampara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=35)),
                ('Consumo', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='ajuste',
            old_name='Emisferio',
            new_name='Hemisferio',
        ),
        migrations.AddField(
            model_name='medicion',
            name='Potencia',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
