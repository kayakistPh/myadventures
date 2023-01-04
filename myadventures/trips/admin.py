from django.contrib import admin
# Register your models here.
from .models import Activity, CombinedTrip, Participents, Trip

admin.site.register(Activity)
#admin.site.register(CombinedTrip)
@admin.register(CombinedTrip)
class CombinedTripAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end')
#admin.site.register(Participents)
@admin.register(Participents)
class ParticipentsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
#admin.site.register(Trip)
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'future', 'display_activity')#, 'display_combined_trip')
