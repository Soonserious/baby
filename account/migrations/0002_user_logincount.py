# Generated by Django 2.1.2 on 2019-08-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='loginCount',
            field=models.IntegerField(default=5),
        ),
    ]