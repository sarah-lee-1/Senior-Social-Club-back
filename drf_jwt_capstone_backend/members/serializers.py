from rest_framework import serializers
from .models import Member 

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ['first_name', 'middle_name', 'last_name', 
                  'email', 'address', 'city', 'zip_code', 
                  'is_active', 'balance']
