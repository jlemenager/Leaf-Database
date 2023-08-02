# Generated by Django 4.2.3 on 2023-07-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0016_alter_ghgassessmentdataperyear_average_business_trip_commute_in_miles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghgassessmentdataperyear',
            name='main_waste_type',
        ),
        migrations.RemoveField(
            model_name='ghgassessmentdataperyear',
            name='total_waste_in_pounds',
        ),
        migrations.AddField(
            model_name='ghgassessmentdataperyear',
            name='other_food_waste_in_pounds',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='ghgassessmentdataperyear',
            name='other_material_waste_in_pounds',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='spendingdataperyear',
            name='cost_of_order_picking',
            field=models.CharField(default='0', max_length=100),
        ),
    ]