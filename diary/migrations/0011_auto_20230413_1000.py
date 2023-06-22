# Generated by Django 3.2.7 on 2023-04-13 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0010_alter_diary_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='event2',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='出来事2'),
        ),
        migrations.AddField(
            model_name='diary',
            name='event3',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='出来事3'),
        ),
        migrations.AddField(
            model_name='diary',
            name='event4',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='出来事2'),
        ),
        migrations.AddField(
            model_name='diary',
            name='event5',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='出来事3'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='event1',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='出来事1'),
        ),
    ]