# Generated by Django 3.0.5 on 2020-05-05 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cel_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cel_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ciudad_residencia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='familiares',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='foto_perfil',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ha_trabajado',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='pais_nacimiento',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
