# admin.py
from django.contrib import admin
from .models import Video, Contact, Booking, Event



admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(Booking)
admin.site.register(Event)