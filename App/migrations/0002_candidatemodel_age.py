# Generated by Django 4.1.3 on 2022-11-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidatemodel",
            name="age",
            field=models.CharField(default=1, max_length=3),
        ),
    ]
