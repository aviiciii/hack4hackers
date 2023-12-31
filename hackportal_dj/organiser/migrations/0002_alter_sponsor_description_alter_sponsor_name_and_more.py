# Generated by Django 4.2.3 on 2023-07-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organiser", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
    ]
