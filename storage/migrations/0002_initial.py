# Generated by Django 5.1.4 on 2024-12-31 23:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='storageowner',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='storagedeals',
            name='storage_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.storageowner'),
        ),
        migrations.AddField(
            model_name='storageownergigs',
            name='storage_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.storageowner'),
        ),
    ]