from django.contrib import admin

from .models import Event, Role

class RoleInline(admin.StackedInline):
    model = Role
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [RoleInline]

admin.site.register(Event, EventAdmin)

# Register your models here.
