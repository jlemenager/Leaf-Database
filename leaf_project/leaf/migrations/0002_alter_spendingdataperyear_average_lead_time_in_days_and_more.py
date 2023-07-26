# Generated by Django 4.2.3 on 2023-07-26 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='average_lead_time_in_days',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='cost_of_using_inventory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='gross_profit_from_item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='items_sold',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='marketing_cost',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='number_in_inventory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='number_of_error_free_freight_bills',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='number_of_freight_bills',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='outstanding_payments_from_customers',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='outstanding_payments_to_suppliers',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='revenue',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spendingdataperyear',
            name='total_shipping_expense',
            field=models.CharField(max_length=100),
        ),
    ]