# Generated by Django 4.2.3 on 2023-07-31 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_consultas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
    ]
