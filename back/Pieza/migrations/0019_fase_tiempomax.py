# Generated by Django 2.1.4 on 2019-02-12 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0018_auto_20190131_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='fase',
            name='tiempoMax',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
