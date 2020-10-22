from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True,related_name='user')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.PositiveIntegerField()

    def __str__(self):
        return f'I am {self.first_name}'


class Expense(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True,related_name='expense')
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True,related_name='expense')

    def __str__(self):
        return f'I am {self.title}'
