# Generated by Django 3.1.4 on 2022-03-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20220318_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=True),
        ),
    ]