from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date


class Person(models.Model):
    """model representing a person."""
    int_code = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    credit = models.PositiveIntegerField(default=0)
    followers = models.ManyToManyField('self', related_name = 'follows', symmetrical=False)
    followings = models.ManyToManyField('self', related_name = 'followis', symmetrical=False)

    def __unicode__(self):
        return u'%s follows %s' % (self.followers, self.followings)

    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular person instance.
    #     """
    #     return reverse('catalog:person-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Transaction(models.Model):
    """model representing a Transaction."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    borrower = models.ForeignKey('Person', related_name = 'borrower', on_delete=models.CASCADE)
    lender = models.ForeignKey('Person', related_name = 'lender', on_delete=models.CASCADE)
    credit = models.PositiveIntegerField(blank=False, null=False)
