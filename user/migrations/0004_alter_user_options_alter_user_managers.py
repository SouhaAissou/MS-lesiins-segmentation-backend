# Generated by Django 5.0.6 on 2024-05-26 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
    ]
