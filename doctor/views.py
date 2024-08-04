from django.shortcuts import render
from rest_framework import viewsets,filters,pagination
from .import models
from .import serializers
# Create your views here.
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100


class DoctorViewset(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serializers.DoctorSerializers
    filter_backends=[filters.SearchFilter]
    pagination_class=DoctorPagination
    search_fieldsd=['user__first_name','user__email','designation__name','specilization__name ']

    def get_queryset(self):
        queryset = super().get_queryset()
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(id=doctor_id)
        return queryset


class SpecializationViewset(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializers


class DesignationViewset(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializers.DesignationSerializers


class ReviewViewset(viewsets.ModelViewSet):

    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializers


class AvailableTimeFilter(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set



class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializers
    filter_backends=[AvailableTimeFilter]
