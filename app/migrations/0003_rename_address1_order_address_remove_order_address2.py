# Generated by Django 4.1.7 on 2023-04-05 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address2',
        ),
    ]
