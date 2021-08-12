from rest_framework import serializers
from Teachers.models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'

class AttnSerializer(serializers.ModelSerializer):
    class Meta:
        model = attandance
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = slots
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'