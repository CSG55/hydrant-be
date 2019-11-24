from django.contrib import admin
from .models.hydrant import Hydrant

class HydrantAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', )

admin.site.register(Hydrant, HydrantAdmin)

# admin.site.register(Hydrant)

