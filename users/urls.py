from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create-user', views.create_user),
    path('delete-user/<str:username>', views.delete_user)

]

