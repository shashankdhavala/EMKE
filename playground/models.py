from django.db import models
from django.db.models import UniqueConstraint
import uuid
class Doctor(models.Model):
    #doctor_id=models.UUIDField(primary_key=True,default=uuid.uuid4().int % 10000,editable=False,unique=True)
    doctor_id = models.IntegerField(primary_key=True, default=uuid.uuid4().int % 100000, editable=False, unique=True)
    email_id=models.EmailField(help_text="We take mail-id for username",max_length=50,unique=True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    #nmc_id = models.IntegerField(help_text = "Enter your IMR registration number")
    #state=models.CharField(help_text="Which state's medical council?",max_length=15)
    #year=models.CharField(max_length=5)
    password = models.CharField(max_length=100,default="password")
    class Meta:
        db_table='Doctor'
class Patient(models.Model):
    CHOICES =(
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),)
    patient_id=models.IntegerField(primary_key=True, default=uuid.uuid4().int % 100000, editable=False, unique=True)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    Age=models.IntegerField()
    Gender=models.CharField(choices=CHOICES,max_length=10)
    UniqueConstraint(fields=['patient_id','doctor_id'],name='p_key')
    class Meta:
        db_table='patient'
 
    
