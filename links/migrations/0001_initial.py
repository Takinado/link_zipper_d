# Generated by Django 4.1.7 on 2023-03-07 09:00

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("session", models.CharField(max_length=32, verbose_name="Сессия")),
                ("url", models.CharField(max_length=1024, verbose_name="Ссылка")),
                (
                    "zipped_url",
                    models.CharField(max_length=128, verbose_name="Сжатая ссылка"),
                ),
                (
                    "clicks",
                    models.IntegerField(default=0, verbose_name="Количество кликов"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
