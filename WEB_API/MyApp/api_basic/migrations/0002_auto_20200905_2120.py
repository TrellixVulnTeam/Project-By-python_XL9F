# Generated by Django 3.1.1 on 2020-09-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=100000),
        ),
    ]
