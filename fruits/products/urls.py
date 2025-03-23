from django.urls import path
from .views import get_products, get_product, add_product, update_product, delete_product

urlpatterns = [
    path('', get_products),
    path('<int:product_id>/', get_product),
    path('add/', add_product),
    path('update/<int:product_id>/', update_product),
    path('delete/<int:product_id>/', delete_product)
]