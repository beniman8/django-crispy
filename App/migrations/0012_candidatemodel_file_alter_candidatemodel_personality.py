# Generated by Django 4.1.3 on 2022-11-27 00:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0011_alter_candidatemodel_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidatemodel",
            name="file",
            field=models.FileField(default=django.utils.timezone.now, upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="candidatemodel",
            name="personality",
            field=models.CharField(
                choices=[
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
    ]
