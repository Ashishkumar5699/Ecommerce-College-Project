# Generated by Django 4.0.1 on 2022-03-01 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_users_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
