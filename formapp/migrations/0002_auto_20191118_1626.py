# Generated by Django 2.2.7 on 2019-11-18 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='name',
            old_name='last_name',
            new_name='Last_name',
        ),
    ]
