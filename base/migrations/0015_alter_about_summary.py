# Generated by Django 3.2.4 on 2021-07-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20210726_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
