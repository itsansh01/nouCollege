# Generated by Django 4.2.4 on 2023-09-14 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('answeredby', models.CharField(max_length=50)),
                ('posteddate', models.CharField(max_length=30)),
                ('qid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('postedby', models.CharField(max_length=50)),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]
