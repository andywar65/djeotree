# Generated by Django 4.0.3 on 2022-06-02 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djeotree", "0005_elementimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="family",
            name="tags",
        ),
    ]
