# Generated by Django 3.2.4 on 2021-09-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_horaluz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaluz',
            name='Mes',
            field=models.PositiveIntegerField(),
        ),
    ]