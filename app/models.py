from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'LOCAL'),
        (3, 'PATROL'),

    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Province(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=124)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Local_Level(models.Model):
    name = models.CharField(max_length=124)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):

    dep_name = models.CharField(max_length=250)

    def __str__(self):
        return self.dep_name


class Employee(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)
    workplace = models.ForeignKey(
        WorkPlace, null=True, on_delete=models.CASCADE)
    appointed_date = models.DateField()
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    vehicle = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Petrolpump(models.Model):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FiscalYear(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FuelExpense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    patrolpump = models.ForeignKey(Petrolpump, on_delete=models.CASCADE)
    fueltype = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    liter = models.FloatField()
    date = models.DateField()
    fiscalyear = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.employee.name
