# Generated by Django 4.1.3 on 2022-11-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0010_candidatemodel_experience_candidatemodel_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidatemodel",
            name="gender",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="candidatemodel",
            name="salary",
            field=models.CharField(max_length=50),
        ),
    ]
