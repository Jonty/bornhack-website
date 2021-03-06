from django.contrib import admin

from .models import Ticket, TicketType


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ticket_type',
        'camp',
        'paid',
    ]

    list_filter = [
        'paid',
        'ticket_type',
        'camp',
    ]


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'available_in',
        'camp',
    ]
