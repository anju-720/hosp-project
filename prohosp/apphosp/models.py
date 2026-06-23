from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User




class Department(models.Model):

    dept_name = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(upload_to='departments/')

    def __str__(self):
        return self.dept_name




class Doctor(models.Model):

    name = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    qualification = models.CharField(max_length=200)

    experience = models.IntegerField()

    image = models.ImageField(upload_to='doctors/')

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    def __str__(self):
        return self.name




class Patient(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=15)

    address = models.TextField()

    age = models.IntegerField()

    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    appointment_date = models.DateField()
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name









class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name