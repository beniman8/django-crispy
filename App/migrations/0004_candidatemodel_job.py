# Generated by Django 4.1.3 on 2022-11-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0003_candidatemodel_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidatemodel",
            name="job",
            field=models.CharField(default="job", max_length=5),
        ),
    ]
