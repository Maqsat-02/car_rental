# Generated by Django 3.2.8 on 2021-11-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(upload_to='static/myapp/img/'),
        ),
    ]
