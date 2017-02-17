from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'amount', 'backorder']

admin.site.register(Item, ItemAdmin)