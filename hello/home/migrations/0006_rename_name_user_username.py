# Generated by Django 4.0.1 on 2022-02-11 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='UserName',
        ),
    ]