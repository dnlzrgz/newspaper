# Generated by Django 4.2.3 on 2023-07-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="banner",
            field=models.ImageField(blank=True, upload_to="banners/"),
        ),
    ]
