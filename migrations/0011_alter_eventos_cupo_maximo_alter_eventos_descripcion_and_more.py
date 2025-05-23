# Generated by Django 5.0.2 on 2025-05-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_escolar_api', '0010_alter_eventos_cupo_maximo_alter_eventos_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='cupo_maximo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='descripcion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='hora_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='hora_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
