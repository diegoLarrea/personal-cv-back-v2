# Generated by Django 3.0.5 on 2020-05-04 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=15, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=1)),
                ('estado_civil', models.CharField(max_length=20)),
                ('pais_nacimiento', models.CharField(max_length=100)),
                ('ciudad_residencia', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cel_1', models.CharField(max_length=50)),
                ('cel_2', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('foto_perfil', models.TextField()),
                ('familiares', models.TextField()),
                ('ha_trabajado', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
