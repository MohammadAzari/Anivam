from django.contrib import admin
from . import models


@admin.register(models.Person)
class PersonAdmin(models.Person):
    list_filter = ('int_code')
    list_display = ('first_name', 'last_name', 'int_code', 'credit')


@admin.register(models.Transaction)
class TransactionAdmin(models.Transaction):
    pass
