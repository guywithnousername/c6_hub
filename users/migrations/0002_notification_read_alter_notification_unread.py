# Generated by Django 4.2.5 on 2023-09-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='unread',
            field=models.JSONField(null=True),
        ),
    ]
