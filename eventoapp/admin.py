from django.contrib import admin
from eventoapp.models import Package,Contact,Event
# Register your models here.

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','detail','image')  # Fields to display in the list view

class ContactAdmin(admin.ModelAdmin): # type: ignore
    list_dispaly=('name','email','message')
class EventAdmin(admin.ModelAdmin): # type: ignore
    list_dispaly=('name','venue','date','time')


admin.site.register(Event,EventAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Contact,ContactAdmin) # type: ignore

