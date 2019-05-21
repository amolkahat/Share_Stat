from django.db import models

# Create your models here.


class UserData(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField()

    def get_password(self):
        return self.password
