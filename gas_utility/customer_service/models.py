from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('resolved', 'Resolved')])
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_requests")
    resolution = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Request #{self.id}"
