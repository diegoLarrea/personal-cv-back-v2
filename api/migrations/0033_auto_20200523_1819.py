# Generated by Django 3.0.5 on 2020-05-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_empleo_fecha_modificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleo',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]