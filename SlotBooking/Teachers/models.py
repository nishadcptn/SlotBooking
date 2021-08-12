from django.db import models
from Student.models import student
# Create your models here.

class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    class Meta:
        db_table = "teacher"

    def __str__(self):
        return self.name


class attandance(models.Model):
    id = models.AutoField(primary_key=True)
    teacher =  models.ForeignKey(teacher ,on_delete=models.CASCADE)
    p_in = models.DateTimeField(auto_now_add=True)
    p_out = models.DateTimeField(null = True, default = None,blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = "attandance"

    def __str__(self):
        return self.id

class slots(models.Model):
    slot = models.CharField(max_length=50,primary_key=True)
    class Meta:
        db_table = "slots"

    def __str__(self):
        return self.slot


class booking(models.Model):
    id = models.AutoField(primary_key=True)
    slot = models.ForeignKey(slots ,on_delete=models.CASCADE)
    student = models.ForeignKey(student ,on_delete=models.CASCADE)
    teacher = models.ForeignKey(teacher ,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "booking"

    def __str__(self):
        return self.id