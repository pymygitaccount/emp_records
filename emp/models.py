from django import forms
from django.db import models

# Create your models here.


class Employee_data(models.Model):
    """Class created for the Employee details as mentioned. """

    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    DOJ = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "emp_data"


# class Employee_Upload(models, model):
#     """Class created to uplaod/import the from csv file."""

#     name = models.CharField(max_length=100)
#     salary = models.IntegerField()
#     company = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     DOJ = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

   
#     def __str__(self):
#         return self.name