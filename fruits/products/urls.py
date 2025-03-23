from django.urls import path
from .views import get_products, get_product, add_product, update_product, delete_product

urlpatterns = [
    path('products/', get_products),
    path('products/<int:product_id>/', get_product),
    path('products/add/', add_product),
    path('products/update/<int:product_id>/', update_product),
    path('products/delete/<int:product_id>/', delete_product)
]