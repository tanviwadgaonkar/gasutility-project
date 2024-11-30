from django import forms
from .models import ServiceRequest

# Form to create a service request
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer', 'service_type', 'description', 'file_attachment', 'status']  # Correct fields

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters.")
        return description

# Form to update service request (for customer support staff)
class ServiceRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'assigned_to', 'resolution']

    def clean_resolution(self):
        resolution = self.cleaned_data.get('resolution')
        if resolution and len(resolution) < 10:
            raise forms.ValidationError("Resolution must be at least 10 characters.")
        return resolution
