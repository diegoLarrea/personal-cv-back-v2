# Generated by Django 3.0.5 on 2020-05-06 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200505_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'permissions': (('api_listar_personas', 'Listar curriculums'), ('api_editar_persona', 'Editar datos personales'))},
        ),
    ]