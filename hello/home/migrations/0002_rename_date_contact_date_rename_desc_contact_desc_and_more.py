# Generated by Django 4.0.1 on 2022-02-10 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='Desc',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Phone',
        ),
    ]