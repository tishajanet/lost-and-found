from django.contrib import admin
from .models import Item, Claim

class ClaimAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'status', 'claim_date')
    list_filter = ('status',)

admin.site.register(Item)
admin.site.register(Claim, ClaimAdmin)