# Generated by Django 4.1.1 on 2022-10-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='id_evento',
            field=models.BigIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submissao',
            name='trabalho',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
