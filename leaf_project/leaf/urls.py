from django.urls import path 
from . import views 
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('business/', views.BusinessList.as_view(), name='business_list'),
    path('business/<int:pk>', views.BusinessDetail.as_view(), name='business_detail'),
    path('spendingdata/', views.SpendingDataPerYearList.as_view(), name='spendingdata_list'),
    path('spendingdata/<int:pk>', views.SpendingDataPerYearDetail.as_view(), name='spendingdata_detail')
]