from django.contrib import admin
from .models import Client
from .forms import ClientForm


class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('name', 'surname', 'email', 'cell_phone', 'date_birth', 'is_active')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('address', 'zip_code')
        })
    )

    list_display = ('name', 'surname', 'email', 'cell_phone')
    search_fields = ('name', 'surname')
    form = ClientForm


admin.site.register(Client, ClienteAdmin)

