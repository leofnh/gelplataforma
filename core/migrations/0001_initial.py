# Generated by Django 4.1.1 on 2022-10-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('data_evento', models.DateTimeField()),
                ('dia1', models.DateTimeField()),
                ('dia2', models.DateTimeField()),
                ('dia3', models.DateTimeField()),
                ('modalidade', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=500)),
                ('p2', models.CharField(max_length=500)),
                ('p3', models.CharField(max_length=500)),
                ('v1', models.BigIntegerField()),
                ('v2', models.BigIntegerField()),
                ('v3', models.BigIntegerField()),
                ('id_evento', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('trabalho', models.FileField(upload_to='')),
            ],
        ),
    ]
