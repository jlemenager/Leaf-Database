# Generated by Django 4.2.3 on 2023-07-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0012_digitalmarketingdataperyear_business_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spendingdataperyear',
            name='cogs',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='spendingdataperyear',
            name='safety_stock',
            field=models.CharField(default='None', max_length=100),
        ),
    ]