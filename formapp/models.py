from django.db import models
class Name(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
