# Generated by Django 4.2 on 2023-04-13 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_like'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='like',
            table='like',
        ),
        migrations.AlterModelTable(
            name='ttag',
            table='ttag',
        ),
    ]
