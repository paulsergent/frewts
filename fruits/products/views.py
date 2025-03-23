import json
from django.http import JsonResponse
from .models import Products
# Create your views here.
def get_products(request):
    products = Products.objects.all()   
    products_list = []
    for product in products:
        products_list.append({
            'name': product.name,
            'description': product.description,
            'quantity': product.quantity,
            'price': product.price,
            'is_available': product.is_available
        })
    return JsonResponse(products_list, safe=False)

def get_product(request, product_id):
    product = Products.objects.get(id=product_id)
    product_dict = {
        'name': product.name,
        'description': product.description,
        'quantity': product.quantity,
        'price': product.price,
        'is_available': product.is_available
    }
    return JsonResponse(product_dict, safe=False)

def add_product(request):
    data = json.loads(request.body)
    product = Products(
        name = data['name'],
        description = data['description'],
        quantity = data['quantity'],
        price = data['price'],
        is_available = data['is_available']
    )
    product.save()
    return JsonResponse({'message': 'Product added successfully'})

def update_product(request, product_id):
    product = Products.objects.get(id=product_id)
    data = json.loads(request.body)
    product.name = data['name']
    product.description = data['description']
    product.quantity = data['quantity']
    product.price = data['price']
    product.is_available = data['is_available']
    product.save()
    return JsonResponse({'message': 'Product updated successfully'})

def delete_product(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    return JsonResponse({'message': 'Product deleted successfully'})
