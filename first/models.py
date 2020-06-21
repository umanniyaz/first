from django.db import models



class Customer(models.Model):
    id=models.IntegerField(max_length=20)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email_id=models.CharField(max_length=200)
    number=models.IntegerField(max_length=200)
    csv = models.FileField(upload_to='customer/csv/')

def __str__(self):
    return self.first_name
