from django.urls import path
from catalog import views

urlpatterns = [
    path('variations/', views.variation_list),
    path('variations/<int:pk>/', views.variation_detail),
]