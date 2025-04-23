from django.db import models
from django.urls import reverse

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

     # Define a method to get the URL for this particular dog instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this dog's details
        return reverse('dog-detail', kwargs={'dog_id': self.id})