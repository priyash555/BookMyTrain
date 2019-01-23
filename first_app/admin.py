from django.contrib import admin
from .models import Register, Train, Ticket, Station, Passenger
# Register your models here.

class StationEntry(admin.ModelAdmin):
    list_display = ("id", "station_name", "train", "arrival_time", "departure_time", "platform")

class TrainEntry(admin.ModelAdmin):
    list_display = ("train_no", "train_name", "source", "destination")

admin.site.register(Register)
admin.site.register(Train, TrainEntry)
admin.site.register(Ticket)
admin.site.register(Passenger)
admin.site.register(Station, StationEntry)
