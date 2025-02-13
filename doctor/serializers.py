from rest_framework import serializers
from . import models

class DoctorSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    specialization=serializers.StringRelatedField(many=True)
    available_time=serializers.StringRelatedField(many=True)
    designation=serializers.StringRelatedField(many=True)
    class Meta:
        model=models.Doctor
        fields='__all__'


class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Specialization
        fields='__all__'


class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Designation
        fields='__all__'


class AvailableTimeSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.AvailableTime
        fields='__all__'

class ReviewSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Review
        fields='__all__'
