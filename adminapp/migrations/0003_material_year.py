# Generated by Django 4.2.4 on 2023-09-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='year',
            field=models.CharField(default=0.0004948045522018803, max_length=100),
            preserve_default=False,
        ),
    ]
