# Generated by Django 5.1.4 on 2025-01-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_alter_storagedeals_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageownergigs',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
