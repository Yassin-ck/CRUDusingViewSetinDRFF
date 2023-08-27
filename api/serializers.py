from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    def alphabetical_validation(value):
        if not value[:3].isalpha():
            raise serializers.ValidationError('Name Should Start With Alphabets')
        return value

    name = serializers.CharField(validators=[alphabetical_validation] )

    class Meta:
        model = Student
        fields = '__all__'
        
