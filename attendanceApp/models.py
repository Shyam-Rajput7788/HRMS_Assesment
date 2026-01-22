from django.db import models
from employeesApp.models import Employee


class Attendance(models.Model):                     
      STATUS_CHOICES = (
      ('Present', 'Present'),
      ('Absent', 'Absent'),
      )
      
      
      employee = models.ForeignKey(
      Employee,
      on_delete=models.CASCADE,
      related_name='attendance_records'
      )
      date = models.DateField()
      status = models.CharField(max_length=10, choices=STATUS_CHOICES)
      
      
class Meta:
      unique_together = ('employee', 'date')