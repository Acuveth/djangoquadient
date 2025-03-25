from django.contrib import admin
from .models import APIConfiguration, BatchRecord, Document, APIRequestLog

admin.site.register(APIConfiguration)
admin.site.register(BatchRecord)
admin.site.register(Document)
admin.site.register(APIRequestLog)