# Generated by Django 4.1.6 on 2023-05-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='music'),
        ),
    ]
