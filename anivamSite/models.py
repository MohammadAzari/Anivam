from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date


class Person(Models.Model):
    """model representing a person."""
    int_code = models.PositiveIntegerField(primary_key=True, max_length=10, blank=False, null=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    credit = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        """
        Returns the url to access a particular person instance.
        """
        return reverse('catalog:person-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Transaction(Models.model):
    """model representing a Transaction."""

    persons = models..ManyToManyField(Person, help_text='please Select two persons for this Transaction')
