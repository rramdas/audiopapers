# Generated by Django 4.2.3 on 2023-07-29 05:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pdfparser", "0002_alter_paper_id_alter_uploadedpaper_pdf"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paper",
            old_name="id",
            new_name="paper_id",
        ),
    ]
