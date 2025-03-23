import json
from django.http import JsonResponse
from .models import Users
# Create your views here.

def get_users(request):
    users = Users.objects.all()
    users_list = []
    for user in users:
        users_list.append({
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'is_active': user.is_active,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        })
    return JsonResponse(users_list, safe=False)

def get_user(request, user_id):
    user = Users.objects.get(id=user_id)
    user_dict = {
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'is_active': user.is_active,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    }
    return JsonResponse(user_dict, safe=False)

def add_user(request):
    data = json.loads(request.body)
    user = Users(
        name = data['name'],
        email = data['email'],
        password = data['password'],
        is_active = data['is_active']
    )
    user.save()
    return JsonResponse({'message': 'User added successfully'})
# 
def update_user(request, user_id):
    user = Users.objects.get(id=user_id)
    data = json.loads(request.body)
    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    user.is_active = data['is_active']
    user.save()
    return JsonResponse({'message': 'User updated successfully'})

def delete_user(request, user_id):
    user = Users.objects.get(id=user_id)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'})

