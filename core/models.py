from email.policy import default
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)
    siret = models.CharField(max_length=14, unique=True)
    postal_code = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Counter(models.Model):
    ELEC = 'ELEC'
    GAZ = 'GAZ'
    PDL_TYPES = [
        (ELEC, 'ELEC'),
        (GAZ, 'GAZ'),
    ]
    
    pdl = models.CharField(max_length=255)
    pdl_type = models.CharField(max_length=50, default=ELEC, choices=PDL_TYPES)

    count_value = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"counter {self.pk}"


class Quotation(models.Model):
    company_name = models.CharField(max_length=100)
    company_reason = models.CharField(max_length=255)
    company_siret = models.CharField(max_length=14)
    company_postal_code = models.CharField(max_length=20)

    manager_first_name = models.CharField(max_length=50)
    manager_last_name = models.CharField(max_length=50)
    manager_phone_number = models.CharField(max_length=8)
    manager_email = models.EmailField(unique=False)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name}-{self.manager_email}"
    