# Generated by Django 3.0.5 on 2020-05-10 14:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0021_auto_20200510_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleo',
            name='postulaciones',
        ),
        migrations.AddField(
            model_name='empleo',
            name='postulantes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='PostulacionEmpleo',
        ),
    ]
