# Generated by Django 4.1.1 on 2022-11-02 14:26

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usuariocd_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='cpfteste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
            ],
        ),
    ]
