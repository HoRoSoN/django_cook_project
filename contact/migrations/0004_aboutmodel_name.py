# Generated by Django 3.2.9 on 2021-11-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_aboutmodel_imageaboutmodel_socialmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
