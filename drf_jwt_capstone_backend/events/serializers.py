from rest_framework import serializers 
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event 
        fields = ('title', 'description', 'month', 'day', 'year', 
                  'time', 'street', 'city', 'state', 'zip_code')
