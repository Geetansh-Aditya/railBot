from django.db import models
import random

class Employee(models.Model):
    employee_id = models.IntegerField(unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50, choices=[
        ('medical', 'Medical'),
        ('cleaning', 'Cleaning'),
        ('electric', 'Electric'),
    ])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = self.generate_unique_employee_id()
        super().save(*args, **kwargs)

    def generate_unique_employee_id(self):
        while True:
            random_id = random.randint(100000, 999999)  # Generates a random 6-digit number
            if not Employee.objects.filter(employee_id=random_id).exists():
                return random_id
