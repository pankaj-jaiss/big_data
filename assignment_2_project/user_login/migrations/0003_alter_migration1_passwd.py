# Generated by Django 4.0.4 on 2022-04-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0002_rename_db_host_migration1_host_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='migration1',
            name='passwd',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
