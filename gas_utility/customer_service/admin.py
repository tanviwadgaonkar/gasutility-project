from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'service_type', 'description', 'date_submitted', 'date_resolved')

    # Display customer name (username from the related User model)
    def customer_name(self, obj):
        return obj.customer.username  # Accessing the related User model for username

    # Display customer email
    def email(self, obj):
        return obj.customer.email  # Accessing the related User model for email

    # Display submission date
    def date_submitted(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M')  # Format date as needed

    # Display resolution date
    def date_resolved(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M')  # Format date as needed

    # Allow sorting by these fields in the admin interface
    customer_name.admin_order_field = 'customer__username'
    email.admin_order_field = 'customer__email'
    date_submitted.admin_order_field = 'created_at'  # Sorting by creation date
    date_resolved.admin_order_field = 'updated_at'  # Sorting by update date

    # Optionally, you can add filters or search fields to make it more usable
    search_fields = ('customer__username', 'service_type', 'description')
    list_filter = ('status', 'assigned_to')

# Register the model with the custom admin interface
admin.site.register(ServiceRequest, ServiceRequestAdmin)
