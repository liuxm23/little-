# Generated by Django 5.1.2 on 2024-10-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("student_id", models.CharField(max_length=255)),
                ("class_name", models.CharField(max_length=255)),
                ("catchphrase", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "people",
            },
        ),
    ]
