# Generated by Django 4.2.1 on 2023-06-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_rename_quete_quote_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
