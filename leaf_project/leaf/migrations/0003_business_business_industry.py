# Generated by Django 4.2.3 on 2023-07-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0002_alter_spendingdataperyear_average_lead_time_in_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_industry',
            field=models.CharField(default='', max_length=100),
        ),
    ]