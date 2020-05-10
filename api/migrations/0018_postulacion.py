# Generated by Django 3.0.5 on 2020-05-09 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0017_delete_postulacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_postulacion', models.DateTimeField(auto_now_add=True)),
                ('empleo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empleo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]