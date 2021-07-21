from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "complete", "priority")
    list_filter = ("created", "complete", "priority")
    search_fields = ("title", "body")
    ordering = ("created", "-complete", "priority")

