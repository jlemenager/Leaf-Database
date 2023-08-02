from rest_framework import serializers
from .models import Business, SpendingDataPerYear,DigitalMarketingDataPerYear,GHGAssessmentDataPerYear, WorkerPayPerYear

class SpendingDataPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business-detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=SpendingDataPerYear
        fields = ('id', 'business', 'business_id', 'business_name', 'item', 'items_sold', 'total_shipping_expense', 'number_in_inventory', 'cost_of_using_inventory', 'marketing_cost', 'outstanding_payments_to_suppliers', 'outstanding_payments_from_customers', 'revenue', 'average_lead_time_in_days', 'number_of_freight_bills', 'number_of_error_free_freight_bills', 'gross_profit_from_item')

class DigitalMarketingDataPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business-detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=DigitalMarketingDataPerYear
        fields = ('id', 'business', 'business_id', 'business_name', 'data_title', 'average_target_age', 'percent_women', 'target_state')
    
class GHGAssessmentDataPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business-detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=GHGAssessmentDataPerYear
        fields = ('id', 'business', 'business_id', 'business_name', 'data_title', 'electricity_from_locations', 'electricity_from_factories', 'average_employee_commute_in_miles', 'employee_count', 'average_business_trip_commute_in_miles', 'total_business_trips', 'total_shipments', 'average_shipment_vehicle_type', 'total_miles_shipped', 'total_water_consumption_in_gallons', 'pounds_of_plastic_used', 'pounds_of_cardboard_used', 'pounds_of_wood_used', 'pounds_of_paper_used', 'pounds_of_metal_used', 'pounds_of_styrofoam_used', 'pounds_of_tetrapaks_used', 'pounds_of_glass_used', 'pounds_of_aluminumfoil_used', 'pounds_of_petplastic_used', 'pounds_of_hdpeplastic_used', 'pounds_of_ldpeplastic_used', 'pounds_of_palmoil_used', 'pounds_of_soybeans_used', 'pounds_of_beef_used', 'pounds_of_rubber_used', 'pounds_of_cocoa_used','other_material_waste_in_pounds', 'other_food_waste_in_pounds')

class WorkerPayPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business-detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=WorkerPayPerYear
        fields = ('id', 'business', 'business_id', 'business_name', 'data_title', 'average_factory_worker_salary_in_thousands_of_dollars', 'average_local_worker_salary_in_thousands_of_dollars', 'average_management_salary_in_thousands_of_dollars')

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    spending_data_per_year = SpendingDataPerYearSerializer(
        # view_name='spending_data_per_year_detail',
        many = True,
        read_only = True
    )

    digital_marketing_data_per_year = DigitalMarketingDataPerYearSerializer(
        # view_name='digital_marketing_data_per_year_detail',
        many = True,
        read_only = True
    )

    ghg_assessment_data_per_year = GHGAssessmentDataPerYearSerializer(
        # view_name='ghg_assessment_data_per_year_detail',
        many = True,
        read_only = True
    )

    worker_pay_per_year = WorkerPayPerYearSerializer(
        # view_name='worker_pay_per_year_detail',
        many = True,
        read_only = True
    )

    business_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'business-detail'
    )

    class Meta:
        model = Business
        fields = ('id', 'business_name', 'business_username', 'business_password', 'spending_data_per_year', 'digital_marketing_data_per_year', 'ghg_assessment_data_per_year', 'worker_pay_per_year', 'business_url', 'is_logged_in')
