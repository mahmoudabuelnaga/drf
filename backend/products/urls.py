from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_create_api_view),
    path('<int:pk>/', views.product_detail_api_view),
]