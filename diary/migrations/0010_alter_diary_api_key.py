# Generated by Django 3.2.7 on 2023-04-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_auto_20230411_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='api_key',
            field=models.CharField(max_length=60, verbose_name='OpenAIのAPI-key'),
        ),
    ]
