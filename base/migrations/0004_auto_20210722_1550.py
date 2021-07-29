# Generated by Django 3.2.4 on 2021-07-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210722_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='sub_description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='sub_title2',
            field=models.CharField(default='NewwWs', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='subject_image2',
            field=models.ImageField(default=1, upload_to='media/%Y%m%d/'),
            preserve_default=False,
        ),
    ]
