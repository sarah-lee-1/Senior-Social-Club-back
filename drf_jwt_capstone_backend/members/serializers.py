from rest_framework import serializers
from .models import Member 

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'middle_name', 'last_name', 
                  'email', 'address', 'city', 'state','zip_code', 
                  'is_active', 'balance')
