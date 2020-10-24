from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    prof = Profile.objects.first().id if Profile.objects.first() else 1
    user = models.ForeignKey(to=Profile, default=prof, on_delete=models.CASCADE,related_name='user')
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='expense')

    def __str__(self):
        return f'I am {self.title}'
