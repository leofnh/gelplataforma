# Generated by Django 4.1.1 on 2022-12-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_delete_cpfteste_rename_id_evento_inscritos_evento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=300)),
            ],
        ),
    ]
