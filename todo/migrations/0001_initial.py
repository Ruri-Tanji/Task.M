# Generated by Django 3.2.5 on 2022-01-07 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('detail', models.TextField(default='')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('map', models.CharField(max_length=256)),
            ],
        ),
    ]
