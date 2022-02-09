from rest_framework import serializers
from .models import SocialClub

class SocialClub(serializers.Serializer):
    
    class Meta:
        model = SocialClub 
        fields = ['name']
