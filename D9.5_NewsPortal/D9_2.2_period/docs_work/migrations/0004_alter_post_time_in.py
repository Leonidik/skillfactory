# Generated by Django 4.0.5 on 2022-08-31 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs_work', '0003_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
