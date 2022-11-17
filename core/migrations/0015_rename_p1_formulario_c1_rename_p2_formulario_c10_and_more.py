# Generated by Django 4.1.1 on 2022-11-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_criterios_avaliadores_data_criacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulario',
            old_name='p1',
            new_name='c1',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='p2',
            new_name='c10',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='p3',
            new_name='c2',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='v1',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='v2',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='v3',
        ),
        migrations.AddField(
            model_name='formulario',
            name='c3',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='c4',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='c5',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='c6',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='c7',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='c8',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='c9',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='data_cadastro',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='formulario',
            name='nome_formulario',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
