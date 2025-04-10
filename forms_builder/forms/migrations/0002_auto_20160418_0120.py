# Generated by Django 1.9.4 on 2016-04-18 01:20
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="email_from",
            field=models.EmailField(
                blank=True,
                help_text="The address the email will be sent from",
                max_length=254,
                verbose_name="From address",
            ),
        ),
    ]
