# Generated by Django 4.1.3 on 2022-12-19 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_alter_documents_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="type",
            name="color",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=7,
                verbose_name="Цвет в HEX",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="documents", name="file", field=models.FileField(upload_to=""),
        ),
        migrations.AddConstraint(
            model_name="type",
            constraint=models.UniqueConstraint(
                fields=("title", "color"), name="unique_tag_name_color"
            ),
        ),
    ]