# Generated by Django 4.1.3 on 2022-11-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0009_candidatemodel_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidatemodel",
            name="experience",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="candidatemodel",
            name="gender",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="candidatemodel",
            name="personality",
            field=models.CharField(
                choices=[
                    ("", "Select a persoanlity type"),
                    ("outgoing", "outgoing"),
                    ("sociable", "sociable"),
                    ("antisocial", "antisocial"),
                    ("discreet", "discreet"),
                    ("serious", "serious"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="candidatemodel",
            name="salary",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="candidatemodel",
            name="smoker",
            field=models.CharField(
                choices=[("1", "Yes"), ("2", "No")],
                default="",
                max_length=10,
                null=True,
            ),
        ),
    ]
