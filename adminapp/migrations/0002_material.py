# Generated by Django 4.2.4 on 2023-09-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='material',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('program', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=255)),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
    ]
