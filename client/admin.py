from django.contrib import admin
from .models import Complaint
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = ('complaint_id', 'client_pnr', 'client_name', 'complaint_time', 'department')

    # Fields to be searchable in the admin search box
    search_fields = ('client_pnr', 'department')

    # Fields to be filterable using the sidebar
    list_filter = ('department',)

    # Fields to be displayed in the detail view
    fields = ('complaint_id', 'client_pnr', 'client_name', 'complaint_time', 'department')

    # Read-only fields in the detail view
    readonly_fields = ('complaint_id','complaint_time',)


admin.site.register(Complaint, ClientAdmin)