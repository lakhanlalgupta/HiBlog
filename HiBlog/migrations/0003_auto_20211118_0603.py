# Generated by Django 3.2.9 on 2021-11-18 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HiBlog', '0002_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.DeleteModel(
            name='NewSubjects',
        ),
    ]
