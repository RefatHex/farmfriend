# Generated by Django 5.1.4 on 2025-01-13 22:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_rentowner_ratings'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentItemOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='rent_gigs/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_ready_for_pickup', models.BooleanField(default=False)),
                ('rent_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rentals.rentowner')),
                ('rent_taker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='RentItemGigs',
        ),
    ]