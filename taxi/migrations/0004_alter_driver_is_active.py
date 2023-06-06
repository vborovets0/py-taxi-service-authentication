# Generated by Django 4.1 on 2023-06-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0003_alter_manufacturer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
