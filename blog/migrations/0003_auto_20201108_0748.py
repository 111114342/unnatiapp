# Generated by Django 3.1.1 on 2020-11-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201108_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
