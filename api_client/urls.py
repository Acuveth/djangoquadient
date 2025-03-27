from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_id>/', views.category, name='category'),
    path('endpoint/<str:endpoint_id>/', views.endpoint_detail, name='endpoint_detail'),
    path('api/call/', views.call_api, name='call_api'),
    path('report/', views.report_query, name='report_query'),  # New URL for report query
    path('batches/', views.batch_list, name='batch_list'),  # New URL for batch list
    path('api/start-batch/', views.start_batch, name='start_batch'),  # API endpoint to start a batch
    path('api/dashboard/delivery-performance/', views.dashboard_delivery_performance, name='dashboard_delivery_performance'),
    path('api/dashboard/engagement-analytics/', views.dashboard_engagement_analytics, name='dashboard_engagement_analytics'),
    path('api/dashboard/device-analytics/', views.dashboard_device_analytics, name='dashboard_device_analytics'),
    path('api/dashboard/batch-device-analytics/', views.batch_device_analytics, name='batch_device_analytics'),
    path('api/dashboard/time-analytics/', views.time_analytics, name='time_analytics'),
    path('api/dashboard/compliance-monitoring/', views.compliance_monitoring, name='compliance_monitoring'),
    path('api/dashboard/batch-compliance-data/', views.batch_compliance_data, name='batch_compliance_data'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
]