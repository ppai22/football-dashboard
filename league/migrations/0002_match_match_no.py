# Generated by Django 3.1 on 2020-09-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_no',
            field=models.IntegerField(default=0),
        ),
    ]
