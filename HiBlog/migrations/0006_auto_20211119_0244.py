# Generated by Django 3.2.9 on 2021-11-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiBlog', '0005_alter_newsubjects_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newsubjects',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]