# Generated by Django 4.1.1 on 2022-11-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_usuariocd_autor_usuariocd_avaliador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariocd',
            name='contato',
            field=models.BigIntegerField(null=True),
        ),
    ]
