# Generated by Django 4.2.5 on 2023-09-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_topic_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='voted',
            field=models.JSONField(null=True),
        ),
    ]
