# Generated by Django 4.2.5 on 2023-09-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_poll_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='values',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
