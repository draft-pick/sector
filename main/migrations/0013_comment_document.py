# Generated by Django 4.1.3 on 2022-12-06 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="document",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_doc",
                to="main.documents",
            ),
            preserve_default=False,
        ),
    ]