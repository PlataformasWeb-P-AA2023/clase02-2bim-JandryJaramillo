# Generated by Django 4.2.2 on 2023-06-12 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0002_estudiante_tipo_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del Pais')),
                ('capital', models.CharField(max_length=30, verbose_name='Capital del Pais')),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='edad',
            field=models.IntegerField(verbose_name='edad de estudiante'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre de estudiante'),
        ),
    ]
