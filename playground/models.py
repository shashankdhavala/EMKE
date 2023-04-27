from django.db import models
class Doctor(models.Model):
    email_id=models.EmailField(help_text="We take mail-id for username",max_length=50)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    nmc_id = models.IntegerField(help_text = "Enter your IMR registration number")
    state=models.CharField(help_text="Which state's medical council?",max_length=15)
    year=models.CharField(max_length=5)
    password = models.CharField(max_length=100,default="password")
    class Meta:
        db_table='Doctor'