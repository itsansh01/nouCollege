# Generated by Django 4.2.4 on 2023-09-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='newsandevents',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='branch',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='news',
            name='ids',
        ),
        migrations.RemoveField(
            model_name='news',
            name='program',
        ),
        migrations.RemoveField(
            model_name='news',
            name='year',
        ),
        migrations.AddField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0.0004972650422675286, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
