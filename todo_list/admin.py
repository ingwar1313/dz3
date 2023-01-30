from django.contrib import admin
from todo_list.models import Task
# Register your models here.
from .models import Task
from django.db.models import Q, Case, Value, When
from datetime import datetime

@admin.action(description="Изменить статус задачи")
def change_task_status(modeladmin, request, queryset):
    """Изменить статус задачи - выполнена или нет"""
    queryset.update(is_active=Q(is_active=False), 
    timestamp_closed=Case(
    When(is_active=True, then=Value(datetime.now())),
    default=Value(None)))

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Отображение модели Task в админке"""
    list_display = (
        "id",
        "name",
        "is_active",
        "timestamp_created",
        "timestamp_closed"
    )
    list_filter = ["is_active"]
    actions = [change_task_status]


