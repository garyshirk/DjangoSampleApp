from django.contrib import admin

from .models import Item

from .models import Staff

class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'amount', 'backorder']

class StaffAdmin(admin.ModelAdmin):
	list_display = ['firstname', 'lastname', 'division', 'timeonjob']

admin.site.register(Item, ItemAdmin)

admin.site.register(Staff, StaffAdmin)