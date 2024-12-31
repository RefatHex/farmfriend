# Generated by Django 5.1.4 on 2024-12-31 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='crops/')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='farmers/')),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('field_size', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('average_rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerGigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='farmer_gigs/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
