from django.urls import path 
from . import views 
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('business/', views.BusinessList.as_view(), name='business_list'),
    path('business/<int:pk>', views.BusinessDetail.as_view(), name='business-detail'),
    path('business/<int:pk>/spendingdata/', views.SpendingDataPerYearList.as_view(), name='spendingdata_list'),
    path('spendingdata/<int:pk>', views.SpendingDataPerYearDetail.as_view(), name='spendingdata_detail'),
    path('business/<int:pk>/marketingdata/', views.DigitalMarketingDataPerYearList.as_view(), name='digitalmarketingdata_list'),
    path('marketingdata/<int:pk>', views.DigitalMarketingDataPerYearDetail.as_view(), name='digitalmarketingdata_detail'),
    path('business/<int:pk>/ghgassessmentdata/', views.GHGAssessmentDataPerYearList.as_view(), name='ghgassessmentdata_list'),
    path('ghgassessmentdata/<int:pk>', views.GHGAssessmentDataPerYearDetail.as_view(), name='ghgassessmentdata_detail'),
    path('workerpaydata/', views.WorkerPayPerYearList.as_view(), name='workerpaydata_list'),
    path('workerpaydata/<int:pk>', views.WorkerPayPerYearDetail.as_view(), name='workerpaydata_detail'),
]