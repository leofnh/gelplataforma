# Generated by Django 4.1.1 on 2022-11-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_avaliadores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterio', models.CharField(max_length=500)),
                ('id_sessao', models.BigIntegerField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='avaliadores',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
