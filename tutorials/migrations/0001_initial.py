# Generated by Django 3.1.1 on 2021-01-12 18:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('summary', models.CharField(max_length=120)),
                ('content', tinymce.models.HTMLField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
