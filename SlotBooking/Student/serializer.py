from rest_framework import serializers
from Student.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'