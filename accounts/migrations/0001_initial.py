# Generated by Django 3.2.9 on 2021-12-13 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('superuser', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=15)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
