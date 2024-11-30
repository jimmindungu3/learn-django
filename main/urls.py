from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='users_home'),
    path('create-user', views.create_user, name='create_user'),
    path('get-users', views.get_all_users, name='get_all_users'),
    path('delete-user/<int:user_id>', views.delete_user, name='delete_user'),
]

