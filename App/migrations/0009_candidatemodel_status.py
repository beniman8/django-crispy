# Generated by Django 4.1.3 on 2022-11-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0008_alter_candidatemodel_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidatemodel",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Disapproved", "Disapproved"),
                ],
                default="Pending",
                max_length=50,
                null=True,
            ),
        ),
    ]