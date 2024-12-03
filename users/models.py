from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    