# Generated by Django 2.0.4 on 2018-04-25 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='thumname_image',
            new_name='thumnail_image',
        ),
    ]
