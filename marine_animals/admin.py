from django.contrib import admin
from .models import SeaAnimal, Aquarium, Employee, Feeding, Ticket, Event

admin.site.register(SeaAnimal)
admin.site.register( Aquarium)
admin.site.register(Employee)
admin.site.register(Feeding)
admin.site.register(Ticket)
admin.site.register(Event)

