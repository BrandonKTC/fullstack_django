# Generated by Django 4.1 on 2023-03-08 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='starts',
            new_name='stars',
        ),
    ]
