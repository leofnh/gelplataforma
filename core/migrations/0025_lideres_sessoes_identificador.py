# Generated by Django 4.1.1 on 2022-12-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_formulario_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lideres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('id_usuario', models.BigIntegerField()),
                ('sessao', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sessoes',
            name='identificador',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]