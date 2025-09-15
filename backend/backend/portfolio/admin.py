from django.contrib import admin
from .models import Projects

@admin.register(Projects)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    search_fields = ('title', 'description')
    list_filter = ('date_added',)
    ordering = ('-date_added',)

    # This will allow the admin form to show file upload for image
    fields = ('title', 'description', 'image', 'live_url')
