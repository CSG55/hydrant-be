from django.contrib import admin
from .models.hydrant import Hydrant
from .models.review import Review

class HydrantAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_by = request.user
        obj.save()

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_by = request.user
        obj.save()

admin.site.register(Hydrant, HydrantAdmin)
admin.site.register(Review, ReviewAdmin)


