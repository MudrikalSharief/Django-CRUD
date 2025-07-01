from django.contrib import admin
from .models import TodoItem

# Register your models here.
admin.site.register(TodoItem)  # Register the TodoItem model to the admin site
