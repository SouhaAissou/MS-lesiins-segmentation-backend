# Generated by Django 5.0.6 on 2024-05-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diagnostic",
            name="date_visit",
            field=models.CharField(
                default="1999-09-09", max_length=255, verbose_name="Date of visit"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="date_of_birth",
            field=models.CharField(
                default="", max_length=255, verbose_name="Date of birth"
            ),
        ),
    ]
