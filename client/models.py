from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    client_pnr = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10)])
    client_name = models.CharField(max_length=10, unique=True)
    complaint_time = models.DateTimeField(auto_now_add=True)
    complaint_summary = models.CharField(max_length=1000, unique=True)
    complaint_status = models.CharField(max_length=10, unique=True)
    complaint_brief = models.TextField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return str(self.complaint_id)
