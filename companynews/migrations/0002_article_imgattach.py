# Generated by Django 3.1.1 on 2020-12-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companynews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imgAttach',
            field=models.ImageField(blank=True, null=True, upload_to='images/userUploads'),
        ),
    ]
