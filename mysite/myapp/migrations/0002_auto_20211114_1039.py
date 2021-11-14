# Generated by Django 3.2.8 on 2021-11-14 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agency',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='agency',
            new_name='company',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.FilePathField(default='front-left-side-47.webp', path='/static/myapp/img'),
            preserve_default=False,
        ),
    ]
