# Generated by Django 5.1.1 on 2024-09-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_email_transfer_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='warehouse',
            field=models.BooleanField(default=False),
        ),
    ]
