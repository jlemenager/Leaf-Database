from django.db import models

# Create your models here.

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_username = models.CharField(max_length=100)
    business_password = models.CharField(max_length=100)
    is_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.business_name

class SpendingDataPerYear(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, 
    related_name='spendingbusinesses',default=1)
    business_name = models.CharField(max_length=100, default='none')
    item = models.CharField(max_length=100)
    items_sold = models.CharField(max_length=100)
    cogs = models.CharField(max_length=100, default='None')
    total_shipping_expense = models.CharField(max_length=100)
    number_in_inventory = models.CharField(max_length=100)
    cost_of_using_inventory = models.CharField(max_length=100)
    cost_of_order_picking = models.CharField(max_length=100, default = '0')
    safety_stock = models.CharField(max_length=100, default= 'None')
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
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='digitalmarketingbusinesses', default=1)
    business_name = models.CharField(max_length=100, default='none')
    data_title = models.CharField(max_length=100)
    average_target_age = models.CharField(max_length=100)
    percent_women = models.CharField(max_length=100)
    target_state = models.CharField(max_length=100)
    website = models.CharField(max_length=100, default='www.google.com')

    def __str__(self):
        return self.data_title
    
class GHGAssessmentDataPerYear(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, 
    related_name='ghgassessmentbusinesses', default=1)
    business_name = models.CharField(max_length=100, default='none')
    data_title = models.CharField(max_length=100)
    electricity_from_locations = models.CharField(max_length=100)
    electricity_from_factories = models.CharField(max_length=100)
    average_employee_commute_in_miles = models.CharField(max_length=100)
    employee_count = models.CharField(max_length=100)
    average_business_trip_commute_in_miles = models.CharField(max_length=100)
    total_business_trips = models.CharField(max_length=100)
    total_shipments = models.CharField(max_length=100)
    average_shipment_vehicle_type = models.CharField(max_length=100)
    total_miles_shipped = models.CharField(max_length=100)
    total_water_consumption_in_gallons = models.CharField(max_length=100)
    pounds_of_plastic_used = models.CharField(max_length=100)
    pounds_of_cardboard_used = models.CharField(max_length=100)
    pounds_of_wood_used = models.CharField(max_length=100)
    pounds_of_paper_used = models.CharField(max_length=100)
    pounds_of_metal_used = models.CharField(max_length=100)
    pounds_of_styrofoam_used = models.CharField(max_length=100)
    pounds_of_tetrapaks_used = models.CharField(max_length=100)
    pounds_of_glass_used = models.CharField(max_length=100)
    pounds_of_aluminumfoil_used = models.CharField(max_length=100)
    pounds_of_petplastic_used = models.CharField(max_length=100)
    pounds_of_hdpeplastic_used = models.CharField(max_length=100)
    pounds_of_ldpeplastic_used = models.CharField(max_length=100)
    pounds_of_palmoil_used = models.CharField(max_length=100)
    pounds_of_soybeans_used = models.CharField(max_length=100)
    pounds_of_beef_used = models.CharField(max_length=100)
    pounds_of_rubber_used = models.CharField(max_length=100)
    pounds_of_cocoa_used = models.CharField(max_length=100)
    other_material_waste_in_pounds = models.CharField(max_length=100, default='0')
    other_food_waste_in_pounds = models.CharField(max_length=100, default='0')

    def __str__(self):
        return self.data_title

class WorkerPayPerYear(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='workerpaybusinesses', default=1)
    business_name = models.CharField(max_length=100, default='none')
    data_title = models.CharField(max_length=100)
    average_factory_worker_salary_in_thousands_of_dollars = models.DecimalField(max_digits=5, decimal_places=4)
    average_local_worker_salary_in_thousands_of_dollars = models.DecimalField(max_digits=5, decimal_places=4)
    average_management_salary_in_thousands_of_dollars = models.DecimalField(max_digits=5, decimal_places=4)

    def __str__(self):
        return self.data_title