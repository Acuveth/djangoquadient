from django.db import models
from django.utils import timezone


class APIConfiguration(models.Model):
    """Stores Quadient API configuration details"""
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255)
    base_url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BatchRecord(models.Model):
    """Stores basic information about batches"""
    batch_id = models.IntegerField(unique=True)
    application_id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    document_count = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    last_sync = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Batch {self.batch_id} - {self.name}"


class Document(models.Model):
    """Stores information about documents within a batch"""
    batch = models.ForeignKey(BatchRecord, on_delete=models.CASCADE, related_name='documents')
    document_id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    file_size = models.IntegerField(default=0)
    content_type = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ('batch', 'document_id')
    
    def __str__(self):
        return f"Document {self.document_id} - {self.name}"


class APIRequestLog(models.Model):
    """Logs API requests for auditing purposes"""
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.method} {self.endpoint} - {self.status_code}"