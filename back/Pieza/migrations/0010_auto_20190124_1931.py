# Generated by Django 2.1.4 on 2019-01-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0009_auto_20190117_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejecucion',
            name='nMaquinas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ejecucion',
            name='nPiezas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]