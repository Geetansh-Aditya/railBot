from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = ('employee_id', 'first_name', 'last_name', 'email', 'department')

    # Fields to be searchable in the admin search box
    search_fields = ('employee_id', 'first_name', 'last_name', 'email', 'department')

    # Fields to be filterable using the sidebar
    list_filter = ('department',)

    # Fields to be displayed in the detail view
    fields = ('employee_id', 'first_name', 'last_name', 'email', 'department')

    # Read-only fields in the detail view
    readonly_fields = ('employee_id',)


admin.site.register(Employee, EmployeeAdmin)
