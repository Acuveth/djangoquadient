from django import forms
from .models import APIConfiguration

class APIConfigurationForm(forms.ModelForm):
    """Form for API configuration settings"""
    
    class Meta:
        model = APIConfiguration
        fields = ['name', 'api_key', 'base_url', 'is_active']
        widgets = {
            'api_key': forms.PasswordInput(render_value=True),
        }


class BatchSearchForm(forms.Form):
    """Form for searching batches"""
    
    application_id = forms.IntegerField(
        label='Application ID',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    batch_id = forms.IntegerField(
        label='Batch ID',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    date_from = forms.DateField(
        label='From Date',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    date_to = forms.DateField(
        label='To Date',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )


class DocumentSearchForm(forms.Form):
    """Form for searching documents within a batch"""
    
    document_id = forms.IntegerField(
        label='Document ID',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    name = forms.CharField(
        label='Document Name',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    content_type = forms.CharField(
        label='Content Type',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )