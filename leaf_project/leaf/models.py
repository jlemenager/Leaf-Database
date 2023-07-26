from django.db import models

# Create your models here.

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_username = models.CharField(max_length=100)
    business_password = models.CharField(max_length=100)
    business_industry = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.business_name

class SpendingDataPerYear(models.Model):
    business_username = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='spendingbusinesses')
    item = models.CharField(max_length=100)
    items_sold = models.CharField(max_length=100)
    total_shipping_expense = models.CharField(max_length=100)
    number_in_inventory = models.CharField(max_length=100)
    cost_of_using_inventory = models.CharField(max_length=100)
    marketing_cost = models.CharField(max_length=100)
    outstanding_payments_to_suppliers = models.CharField(max_length=100)
    outstanding_payments_from_customers = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    average_lead_time_in_days = models.CharField(max_length=100)
    number_of_freight_bills = models.CharField(max_length=100)
    number_of_error_free_freight_bills = models.CharField(max_length=100)
    gross_profit_from_item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class DigitalMarketingDataPerYear(models.Model):
    business_username = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='digitalmarketingbusinesses')
    data_title = models.CharField(max_length=100)
    average_target_age = models.IntegerField()
    percent_women = models.DecimalField(max_digits=5, decimal_places=4)
    target_state = models.CharField(max_length=100)

    def __str__(self):
        return self.data_title
    
class GHGAssessmentDataPerYear(models.Model):
    business_username = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='ghgassessmentgbusinesses')
    data_title = models.CharField(max_length=100)
    electricity_from_locations = models.DecimalField(max_digits=5, decimal_places=4)
    electricity_from_factories = models.DecimalField(max_digits=5, decimal_places=4)
    average_employee_commute_in_miles = models.IntegerField()
    employee_count = models.IntegerField()
    average_business_trip_commute_in_miles = models.IntegerField()
    total_business_trips = models.IntegerField()
    total_shipments = models.IntegerField()
    average_shipment_vehicle_type = models.CharField(max_length=100)
    total_miles_shipped = models.IntegerField()
    total_waste_in_pounds = models.CharField(max_length=100)
    main_waste_type = models.CharField(max_length=100)
    total_water_consumption_in_gallons = models.IntegerField()
    pounds_of_plastic_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_cardboard_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_wood_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_paper_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_metal_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_styrofoam_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_tetrapaks_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_glass_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_aluminumfoil_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_petplastic_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_hdpeplastic_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_ldpeplastic_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_palmoil_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_soybeans_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_beef_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_rubber_used = models.DecimalField(max_digits=5, decimal_places=4)
    pounds_of_cocoa_used = models.DecimalField(max_digits=5, decimal_places=4)

    def __str__(self):
        return self.data_title

class WorkerPayPerYear(models.Model):
    business_username = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='workerpaybusinesses')
    data_title = models.CharField(max_length=100)
    average_factory_worker_salary_in_thousands_of_dollars = models.DecimalField(max_digits=5, decimal_places=4)
    average_local_worker_salary_in_thousands_of_dollars = models.DecimalField(max_digits=5, decimal_places=4)
    average_management_salary_in_thousands_of_dollars = models.DecimalField(max_digits=5, decimal_places=4)

    def __str__(self):
        return self.data_title