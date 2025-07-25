# Generated by Django 4.1.4 on 2023-01-07 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="operators",
        ),
        migrations.AddField(
            model_name="team",
            name="task",
            field=models.ManyToManyField(blank=True, null=True, to="teams.task"),
        ),
        migrations.AlterField(
            model_name="loction",
            name="last_location",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="loction",
            name="main_location",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="loction",
            name="more_location",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
