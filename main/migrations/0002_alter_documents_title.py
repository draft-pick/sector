# Generated by Django 4.1.3 on 2022-11-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documents",
            name="title",
            field=models.CharField(max_length=500, verbose_name="Название"),
        ),
    ]
