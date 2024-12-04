from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("get-users", views.get_all_users),
    path('create-user', views.create_user),
    path('update-user/<int:user_id>', views.update_user),
    path('delete-user/<int:user_id>', views.delete_user)
]

