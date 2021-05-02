from django.db import models

# Create your models here.


class AdmissionTeamDB(models.Model):
    email = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=35, blank=False)
    first_name = models.CharField(max_length=15, blank=False)
    middle_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=False)
    dob = models.DateField()
    present_address_street = models.CharField(max_length=15)
    present_address_city = models.CharField(max_length=15)
    present_address_zipCode = models.IntegerField(blank=False)
    present_address_state = models.CharField(max_length=15)
    permanent_address_street = models.CharField(max_length=15)
    permanent_address_city = models.CharField(max_length=15)
    permanent_address_zipCode = models.IntegerField(blank=False)
    permanent_address_state = models.CharField(max_length=15)
    mobile_number = models.IntegerField()
    previous_employment = models.CharField(max_length=20)
    yearsOfExperience = models.DecimalField(decimal_places=2, max_digits=2)
    account_status = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.email

