from django.db import models

# Create your models here.

class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    class Meta:
        db_table = "student"

    def __str__(self):
        return self.name

