# Generated by Django 4.2.3 on 2023-07-25 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_username', models.CharField(max_length=100)),
                ('business_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpendingDataPerYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('items_sold', models.IntegerField()),
                ('total_shipping_expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_in_inventory', models.IntegerField()),
                ('cost_of_using_inventory', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marketing_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outstanding_payments_to_suppliers', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outstanding_payments_from_customers', models.DecimalField(decimal_places=2, max_digits=10)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_lead_time_in_days', models.IntegerField()),
                ('number_of_freight_bills', models.IntegerField()),
                ('number_of_error_free_freight_bills', models.IntegerField()),
                ('gross_profit_from_item', models.DecimalField(decimal_places=2, max_digits=10)),
                ('business_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='leaf.business')),
            ],
        ),
    ]
