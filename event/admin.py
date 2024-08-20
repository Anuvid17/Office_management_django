from django.contrib import admin
from .models import Event, Registration, UserProfile

admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(UserProfile)