from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    