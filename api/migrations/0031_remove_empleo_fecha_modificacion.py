# Generated by Django 3.0.5 on 2020-05-23 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20200523_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleo',
            name='fecha_modificacion',
        ),
    ]