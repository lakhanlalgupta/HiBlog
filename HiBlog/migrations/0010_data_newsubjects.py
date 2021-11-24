# Generated by Django 3.2.9 on 2021-11-24 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HiBlog', '0009_auto_20211123_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('topic_heading', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('paragraph', models.CharField(max_length=10000)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='blogimages/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiBlog.newsubjects')),
            ],
        ),
    ]
