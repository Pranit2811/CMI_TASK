from chunked_upload.models import ChunkedUpload
from django.db import models

MyChunkedUpload = ChunkedUpload

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    size_range = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=255)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'company_details' 
