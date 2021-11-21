# Generated by Django 3.2.8 on 2021-11-21 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=10)),
                ('mileage', models.BigIntegerField()),
                ('number_pass', models.IntegerField()),
                ('per_day', models.IntegerField()),
                ('stereo', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/static/myapp/img')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('date_out', models.DateField()),
                ('date_return', models.DateField()),
                ('day_cost', models.IntegerField()),
                ('Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vehicle')),
            ],
        ),
    ]
