# Generated by Django 4.1.7 on 2023-04-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]