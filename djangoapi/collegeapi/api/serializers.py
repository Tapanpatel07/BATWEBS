from rest_framework import serializers
from api.models import college,Student

class collegeserializer(serializers.HyperlinkedModelSerializer):
    college_id=serializers.ReadOnlyField()
    class Meta:
        model=college
        fields="__all__"

class Studentseriallizer(serializers.HyperlinkedModelSerializer):
    Stu_id=serializers.ReadOnlyField()
        
    class Meta:
        model=Student
        fields="__all__"