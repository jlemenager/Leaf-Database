from django.shortcuts import render
from .models import Business, SpendingDataPerYear
from django.http import JsonResponse
from rest_framework import generics
from .serializers import BusinessSerializer, SpendingDataPerYearSerializer
# Create your views here.

def business_list(request):
    businesses = Business.objects.all().values('business_name', 'business_username') # only grab some attributes from our database, else we can't serialize it.
    businesses_list = list(businesses) # convert our artists to a list instead of QuerySet
    return JsonResponse(businesses_list, safe=False)

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class SpendingDataPerYearList(generics.ListCreateAPIView):
    queryset = SpendingDataPerYear.objects.all()
    serializer_class = SpendingDataPerYearSerializer

class SpendingDataPerYearDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpendingDataPerYear.objects.all()
    serializer_class = SpendingDataPerYearSerializer

