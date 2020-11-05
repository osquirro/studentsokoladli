# Generated by Django 2.2.6 on 2020-10-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(blank=True, db_column='matricula', null=True)),
                ('password', models.CharField(blank=True, db_column='password', max_length=15, null=True)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=80, null=True)),
                ('apellidoP', models.CharField(blank=True, db_column='apellidoP', max_length=80, null=True)),
                ('apellidoM', models.CharField(blank=True, db_column='apellidoM', max_length=80, null=True)),
                ('grado', models.IntegerField(blank=True, db_column='grado', null=True)),
                ('grupo', models.CharField(blank=True, db_column='grupo', max_length=1, null=True)),
                ('nombreP', models.CharField(blank=True, db_column='nombreP', max_length=80, null=True)),
                ('apellidoPP', models.CharField(blank=True, db_column='apellidoPP', max_length=80, null=True)),
                ('apellidoMP', models.CharField(blank=True, db_column='apellidoMP', max_length=80, null=True)),
            ],
        ),
    ]