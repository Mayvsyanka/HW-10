# Generated by Django 4.2.1 on 2023-06-26 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quete',
            new_name='quote',
        ),
    ]
