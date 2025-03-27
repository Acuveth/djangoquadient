import logging
import requests
from django.conf import settings
from django.utils import timezone
from .models import APIRequestLog, BatchRecord

logger = logging.getLogger(__name__)

class QuadientAPIClient:
    """
    Client for interacting with the Quadient Digital Services REST API
    """
    
    def __init__(self, config=None):
        """
        Initialize the API client
        
        Args:
            config: APIConfiguration instance or None to use settings
        """
        if config:
            self.base_url = config.base_url
            self.api_key = config.api_key
        else:
            self.base_url = settings.QUADIENT_API_BASE_URL
            self.api_key = settings.QUADIENT_API_KEY
            
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
    
    def _log_request(self, endpoint, method, request_data, response=None, error=None):
        """
        Log API request and response/error
        """
        try:
            status_code = None
            response_data = None
            error_message = None
            
            if response:
                status_code = response.status_code
                try:
                    response_data = response.json()
                except ValueError:
                    response_data = {'raw': 'Unable to parse JSON response'}
            
            if error:
                error_message = str(error)
            
            APIRequestLog.objects.create(
                endpoint=endpoint,
                method=method,
                request_data=request_data,
                response_data=response_data,
                status_code=status_code,
                error_message=error_message
            )
        except Exception as e:
            logger.error(f"Failed to log API request: {str(e)}")
    
    def make_request(self, endpoint, method='POST', data=None):
        """
        Make a request to the Quadient API
        
        Args:
            endpoint: API endpoint path
            method: HTTP method (POST, GET, etc.)
            data: Request data dict
            
        Returns:
            Response object or None on error
        """
        try:
            url = f"{self.base_url}{endpoint}"
            
            if method == 'POST':
                response = requests.post(url, headers=self.headers, json=data)
            elif method == 'GET':
                response = requests.get(url, headers=self.headers, params=data)
            else:
                raise ValueError(f"Unsupported method: {method}")
                
            self._log_request(endpoint, method, data, response=response)
            response.raise_for_status()
            return response
        
        except requests.exceptions.RequestException as e:
            self._log_request(endpoint, method, data, error=e)
            logger.error(f"API request failed: {str(e)}")
            return None
    
    def list_batches(self, application_id):
        """
        Get a list of batches for an application
        
        Args:
            application_id: Quadient application ID
            
        Returns:
            List of batch data or empty list on error
        """
        data = {
            "applicationId": application_id
        }
        
        response = self.make_request('/api/query/MobileBackend/ContentListWithFilterV4', 'POST', data)
        
        if response and response.status_code == 200:
            result = response.json()
            # Update our local database with the batch data
            self._update_batch_records(result.get('documents', []), application_id)
            return result.get('documents', [])
        
        return []
    
    def get_batch_details(self, batch_id, application_id):
        """
        Get detailed information about a specific batch
        
        Args:
            batch_id: Batch ID
            application_id: Application ID
            
        Returns:
            Batch details dict or None on error
        """
        data = {
            "applicationId": application_id,
            "filter": {
                "documentIds": [batch_id]
            }
        }
        
        response = self.make_request('/api/query/MobileBackend/ContentListWithFilterV4', 'POST', data)
        
        if response and response.status_code == 200:
            result = response.json()
            documents = result.get('documents', [])
            if documents:
                return documents[0]
        
        return None
    
    def get_document_content(self, document_id, application_id):
        """
        Get binary content of a document
        
        Args:
            document_id: Document ID
            application_id: Application ID
            
        Returns:
            Document binary content or None on error
        """
        data = {
            "documentId": document_id,
            "applicationId": application_id
        }
        
        response = self.make_request('/api/query/MobileBackend/ContentGetBinary', 'POST', data)
        
        if response and response.status_code == 200:
            return response.content
        
        return None
    
    def get_document_metadata(self, document_id, application_id):
        """
        Get document metadata
        
        Args:
            document_id: Document ID
            application_id: Application ID
            
        Returns:
            Document metadata dict or None on error
        """
        data = {
            "documentId": document_id,
            "applicationId": application_id
        }
        
        response = self.make_request('/api/query/MobileBackend/ContentMetadataV3', 'POST', data)
        
        if response and response.status_code == 200:
            return response.json()
        
        return None
    
    def _update_batch_records(self, documents, application_id):
        """
        Update local database with batch records
        
        Args:
            documents: List of document data from API
            application_id: Application ID
        """
        for doc in documents:
            try:
                batch, created = BatchRecord.objects.update_or_create(
                    batch_id=doc['documentId'],
                    defaults={
                        'application_id': application_id,
                        'name': doc.get('name', f"Batch {doc['documentId']}"),
                        'created_at': timezone.datetime.fromtimestamp(
                            int(doc.get('created', '').replace('/Date(', '').replace(')/', '')) / 1000,
                            tz=timezone.utc
                        ) if doc.get('created') else timezone.now(),
                        'document_count': doc.get('externalResourcesCount', 0),
                        'status': 'Active',  # Default status
                        'last_sync': timezone.now()
                    }
                )
                
                # You could also create Document objects here if needed
            except Exception as e:
                logger.error(f"Failed to update batch record: {str(e)}")