# Generated by Django 5.1.4 on 2025-01-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_responses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertairesponse',
            name='answer_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recairesponse',
            name='answer_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]