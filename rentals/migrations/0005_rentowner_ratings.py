# Generated by Django 5.1.4 on 2025-01-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_alter_rentitemgigs_image_alter_rentitems_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentowner',
            name='ratings',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
    ]