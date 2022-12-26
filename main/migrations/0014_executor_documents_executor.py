# Generated by Django 4.1.3 on 2022-12-06 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0013_comment_document"),
    ]

    operations = [
        migrations.CreateModel(
            name="Executor",
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
                ("name", models.CharField(max_length=255, verbose_name="ФИО")),
            ],
            options={
                "verbose_name": "Исполнитель",
                "verbose_name_plural": "Исполнители",
            },
        ),
        migrations.AddField(
            model_name="documents",
            name="executor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="executor_document",
                to="main.executor",
            ),
        ),
    ]
