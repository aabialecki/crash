from django.db import models
from django.contrib.auth.models import User

class Stats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=1000)

    def __str__(self):
        string = str(self.user.username) + ": $" + str(self.balance)
        return string





