from django.contrib import admin
from . models import PersonDetails
from . models import Team,Demo

# Register your models here.

admin.site.register(PersonDetails)
admin.site.register(Team)
admin.site.register(Demo)
