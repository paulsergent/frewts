from django.urls import path
from .views import get_users, get_user, add_user, update_user, delete_user

urlpatterns = [
    path('users/', get_users),
    path('users/<int:user_id>/', get_user),
    path('users/add/', add_user),
    path('users/update/<int:user_id>/', update_user),
    path('users/delete/<int:user_id>/', delete_user)
]