from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)
    siret = models.CharField(max_length=100)
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
    pdl = models.CharField(max_length=255)
    count_value = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"counter {self.pk}"
