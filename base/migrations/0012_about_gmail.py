# Generated by Django 3.2.4 on 2021-07-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_about_image_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='gmail',
            field=models.URLField(blank=True),
        ),
    ]
