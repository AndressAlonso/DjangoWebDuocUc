# Generated by Django 5.0.6 on 2024-07-18 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_producto_almacenamiento_producto_pantalla_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=255),
        ),
    ]
