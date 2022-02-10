from django.contrib import admin
from events.models import Event
from members.models import Member 
# from social_clubs.models import SocialClub 

# Register your models here.
admin.site.register(Event)
admin.site.register(Member)
# admin.site.register(SocialClub)
