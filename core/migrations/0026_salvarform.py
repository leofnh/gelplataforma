# Generated by Django 4.1.1 on 2022-12-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_lideres_sessoes_identificador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salvarform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterio', models.CharField(max_length=150)),
                ('nota', models.BigIntegerField()),
                ('id_avaliado', models.BigIntegerField()),
                ('data_avaliado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
