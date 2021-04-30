from django.contrib import admin
from paste.models import Paste

@admin.register(Paste)
class AdminPaste(admin.ModelAdmin):
    list_display = ["url", "created_at" ]
    ordering = ["created_at"]
