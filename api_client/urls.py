from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_id>/', views.category, name='category'),
    path('endpoint/<str:endpoint_id>/', views.endpoint_detail, name='endpoint_detail'),
    path('api/call/', views.call_api, name='call_api'),
]