# Generated by Django 4.2.1 on 2023-06-02 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_alter_reserva_cliente_alter_reserva_coordinador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='activo',
        ),
    ]