# Generated by Django 3.2.9 on 2021-11-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiBlog', '0006_auto_20211119_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='pic',
            field=models.ImageField(blank=True, upload_to='blogimages'),
        ),
    ]
