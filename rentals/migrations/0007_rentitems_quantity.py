# Generated by Django 5.1.4 on 2025-01-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_rentitemorders_delete_rentitemgigs'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
