# Generated by Django 3.2.9 on 2021-11-18 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HiBlog', '0003_auto_20211118_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('paragraph', models.CharField(max_length=10000)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiBlog.newsubjects')),
            ],
        ),
    ]
