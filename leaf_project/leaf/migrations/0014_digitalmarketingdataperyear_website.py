# Generated by Django 4.2.3 on 2023-07-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0013_spendingdataperyear_cogs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalmarketingdataperyear',
            name='website',
            field=models.CharField(default='www.google.com', max_length=100),
        ),
    ]
