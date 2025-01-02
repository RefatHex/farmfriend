# Generated by Django 5.1.4 on 2024-12-31 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FertAIResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitrogen', models.FloatField()),
                ('phosphorus', models.FloatField()),
                ('potassium', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('moisture', models.FloatField()),
                ('crop_type', models.CharField(max_length=255)),
                ('soil_type', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('asked_at', models.DateTimeField(auto_now_add=True)),
                ('answer_rating', models.FloatField()),
                ('session_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecAIResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitrogen', models.FloatField()),
                ('phosphorus', models.FloatField()),
                ('potassium', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('ph', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('answer', models.CharField(max_length=255)),
                ('asked_at', models.DateTimeField(auto_now_add=True)),
                ('answer_rating', models.FloatField()),
                ('session_id', models.BigIntegerField()),
            ],
        ),
    ]