from django.shortcuts import render
from rest_framework import viewsets
from api.models import college,Student
from api.serializers import collegeserializer,Studentseriallizer

# Create your views here.
class collegeviewset(viewsets.ModelViewSet):
    queryset=college.objects.all()
    serializer_class=collegeserializer

class Studentviewset(viewsets.ModelViewSet):
    queryset=college.objects.all()
    serializer_class=Studentseriallizer
