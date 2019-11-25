from django.contrib import admin
from .models.hydrant import Hydrant
from .models.review import Review

class HydrantAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'created_by')

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'created_by')

admin.site.register(Hydrant, HydrantAdmin)
admin.site.register(Review, ReviewAdmin)


