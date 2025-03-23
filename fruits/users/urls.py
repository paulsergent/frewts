from django.urls import path
from .views import get_users, get_user, add_user, update_user, delete_user

urlpatterns = [
    path('', get_users),
    path('<int:user_id>/', get_user),
    path('add/', add_user),
    path('update/<int:user_id>/', update_user),
    path('delete/<int:user_id>/', delete_user)
]