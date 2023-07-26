from rest_framework import serializers
from .models import Business, SpendingDataPerYear,DigitalMarketingDataPerYear,GHGAssessmentDataPerYear

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    spending_data_per_year = serializers.HyperlinkedRelatedField(
        view_name='spending_data_per_year_detail',
        many = True,
        read_only = True
    )

    business_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'business_detail'
    )

    class Meta:
        model = Business
        fields = ('business_name', 'business_username', 'business_password', 'spending_data_per_year', 'business_url')


class SpendingDataPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business_detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=SpendingDataPerYear
        fields = ('business_username', 'business', 'business_id', 'item', 'items_sold', 'total_shipping_expense', 'number_in_inventory', 'cost_of_using_inventory', 'marketing_cost', 'outstanding_payments_to_suppliers', 'outstanding_payments_from_customers', 'revenue', 'average_lead_time_in_days', 'number_of_freight_bills', 'number_of_error_free_freight_bills', 'gross_profit_from_item')

class DigitalMarketingDataPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business_detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=DigitalMarketingDataPerYear
        fields = ('business_username', 'business', 'business_id', 'data_title', 'average_target_age', 'percent_women', 'target_state')
    
class GHGAssessmentDataPerYearSerializer(serializers.HyperlinkedModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business_detail',
        read_only=True
    )

    business_id = serializers.PrimaryKeyRelatedField(
        queryset = Business.objects.all(),
        source = 'business'
    )

    class Meta:
        model=GHGAssessmentDataPerYear
        fields = ('business_username', 'business', 'business_id', 'data_title', 'electricity_from_locations', 'electricity_from_factories', 'average_employee_commute_in_miles', 'employee_count', 'average_business_trip_commute_in_miles', 'total_business_trips', 'total_shipments', 'average_shipment_vehicle_type', 'total_miles_shipped', 'total_waste_in_pounds', 'main_waste_type', 'total_water_consumption_in_gallons', 'pounds_of_plastic_used', 'pounds_of_cardboard_used', 'pounds_of_wood_used', 'pounds_of_paper_used', 'pounds_of_metal_used', 'pounds_of_styrofoam_used', 'pounds_of_tetrapaks_used', 'pounds_of_glass_used', 'pounds_of_aluminumfoil_used', 'pounds_of_petplastic_used', 'pounds_of_hdpeplastic_used', 'pounds_of_ldpeplastic_used', 'pounds_of_palmoil_used', 'pounds_of_soybeans_used', 'pounds_of_beef_used', 'pounds_of_rubber_used', 'pounds_of_cocoa_used')
    