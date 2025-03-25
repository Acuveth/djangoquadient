import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Get API settings from Django settings
API_BASE_URL = settings.QUADIENT_API_BASE_URL
API_KEY = settings.QUADIENT_API_KEY

def index(request):
    """Home page view with categories of API endpoints"""
    # Categories based on the OpenAPI spec tags
    categories = [
        {"id": "client-content-delivery", "name": "Client - Content Delivery"},
        {"id": "client-data-communication", "name": "Client - Data Communication"},
        {"id": "client-dc-states", "name": "Client - DC States"},
        {"id": "client-identity-providers", "name": "Client - Identity Providers and Authentication"},
        {"id": "client-push-notifications", "name": "Client - Mobile Push Notifications"},
        {"id": "client-user-management", "name": "Client - User Account Management"},
        {"id": "client-other", "name": "Client - Other"},
        {"id": "enterprise-client-management", "name": "Enterprise - Client Management"},
        {"id": "enterprise-content-delivery", "name": "Enterprise - Content Delivery"},
        {"id": "enterprise-data-communication", "name": "Enterprise - Data Communication"},
        {"id": "enterprise-dc-states", "name": "Enterprise - DC States"},
        {"id": "enterprise-other", "name": "Enterprise - Other"},
        {"id": "server-availability", "name": "Server Availability"},
    ]
    
    return render(request, 'api_client/index.html', {
        'categories': categories
    })

def category(request, category_id):
    """View for displaying endpoints in a specific category"""
    # Map of category IDs to their full names
    category_names = {
        "client-content-delivery": "Client - Content Delivery",
        "client-data-communication": "Client - Data Communication",
        "client-dc-states": "Client - DC States",
        "client-identity-providers": "Client - Identity Providers and Authentication",
        "client-push-notifications": "Client - Mobile Push Notifications",
        "client-user-management": "Client - User Account Management",
        "client-other": "Client - Other",
        "enterprise-client-management": "Enterprise - Client Management",
        "enterprise-content-delivery": "Enterprise - Content Delivery",
        "enterprise-data-communication": "Enterprise - Data Communication",
        "enterprise-dc-states": "Enterprise - DC States",
        "enterprise-other": "Enterprise - Other",
        "server-availability": "Server Availability",
    }
    
    # Endpoints mapping for each category
    endpoints = get_endpoints_for_category(category_id)
    
    return render(request, 'api_client/category.html', {
        'category_name': category_names.get(category_id, "Unknown Category"),
        'endpoints': endpoints
    })

def get_endpoints_for_category(category_id):
    """Returns list of endpoints for a given category"""
    # This is a complete mapping of categories to endpoints
    endpoints_map = {
        "client-content-delivery": [
            {"id": "content-delete-by-client", "name": "ContentDeleteByClient", "method": "POST", "path": "/api/publish/MobileBackend/ContentDeleteByClient"},
            {"id": "content-publish-document", "name": "ContentPublishDocument", "method": "POST", "path": "/api/publish/MobileBackend/ContentPublishDocument"},
            {"id": "create-update-metadata-v3", "name": "CreateOrUpdateContentMetadataV3", "method": "POST", "path": "/api/publish/MobileBackend/CreateOrUpdateContentMetadataV3"},
            {"id": "content-get-binary", "name": "ContentGetBinary", "method": "POST", "path": "/api/query/MobileBackend/ContentGetBinary"},
            {"id": "content-get-history", "name": "ContentGetHistory", "method": "POST", "path": "/api/query/MobileBackend/ContentGetHistory"},
            {"id": "content-get-resources", "name": "ContentGetResources", "method": "POST", "path": "/api/query/MobileBackend/ContentGetResources"},
            {"id": "content-list-resources", "name": "ContentListResources", "method": "POST", "path": "/api/query/MobileBackend/ContentListResources"},
            {"id": "content-list-users", "name": "ContentListUsers", "method": "POST", "path": "/api/query/MobileBackend/ContentListUsers"},
            {"id": "content-list-v3", "name": "ContentListV3", "method": "POST", "path": "/api/query/MobileBackend/ContentListV3"},
            {"id": "content-metadata-get-file", "name": "ContentMetadataGetFile", "method": "POST", "path": "/api/query/MobileBackend/ContentMetadataGetFile"},
            {"id": "content-metadata-v3", "name": "ContentMetadataV3", "method": "POST", "path": "/api/query/MobileBackend/ContentMetadataV3"},
            {"id": "get-detached-document", "name": "GetDetachedDocument", "method": "POST", "path": "/api/query/MobileBackend/GetDetachedDocument"},
        ],
        "client-data-communication": [
            {"id": "retrieve-reply-data", "name": "RetrieveReplyData", "method": "POST", "path": "/api/longpoll/MobileBackend/RetrieveReplyData"},
            {"id": "store-and-retrieve-reply-data", "name": "StoreAndRetrieveReplyData", "method": "POST", "path": "/api/longpoll/MobileBackend/StoreAndRetrieveReplyData"},
            {"id": "store-incoming-data", "name": "StoreIncomingData", "method": "POST", "path": "/api/publish/MobileBackend/StoreIncomingData"},
        ],
        "client-dc-states": [
            {"id": "assign-dc-state-to-user", "name": "AssignDcStateToUser", "method": "POST", "path": "/api/publish/MobileBackend/AssignDcStateToUser"},
            {"id": "content-delete-dc-state", "name": "ContentDeleteDcState", "method": "POST", "path": "/api/publish/MobileBackend/ContentDeleteDcState"},
            {"id": "content-store-dc-state", "name": "ContentStoreDcState", "method": "POST", "path": "/api/publish/MobileBackend/ContentStoreDcState"},
            {"id": "content-update-dc-state", "name": "ContentUpdateDcState", "method": "POST", "path": "/api/publish/MobileBackend/ContentUpdateDcState"},
            {"id": "content-get-dc-state", "name": "ContentGetDcState", "method": "POST", "path": "/api/query/MobileBackend/ContentGetDcState"},
            {"id": "content-list-dc-state", "name": "ContentListDcState", "method": "POST", "path": "/api/query/MobileBackend/ContentListDcState"},
            {"id": "content-list-dc-states", "name": "ContentListDcStates", "method": "POST", "path": "/api/query/MobileBackend/ContentListDcStates"},
        ],
        "client-identity-providers": [
            {"id": "delete-identity-provider-association", "name": "DeleteIdentityProviderAssociation", "method": "POST", "path": "/api/publish/MobileBackend/DeleteIdentityProviderAssociation"},
            {"id": "save-identity-user-issue-association-token", "name": "SaveIdentityUserIssueAssociationToken", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserIssueAssociationToken"},
            {"id": "send-otp-anonymous", "name": "SendOtpAnonymous", "method": "POST", "path": "/api/publish/MobileBackend/SendOtpAnonymous"},
            {"id": "send-otp-identity-user", "name": "SendOtpIdentityUser", "method": "POST", "path": "/api/publish/MobileBackend/SendOtpIdentityUser"},
            {"id": "send-otp-two-factor", "name": "SendOtpTwoFactor", "method": "POST", "path": "/api/publish/MobileBackend/SendOtpTwoFactor"},
            {"id": "get-client-id", "name": "GetClientId", "method": "POST", "path": "/api/query/MobileBackend/GetClientId"},
            {"id": "identity-provider-sign-in-data", "name": "IdentityProviderSignInData", "method": "POST", "path": "/api/query/MobileBackend/IdentityProviderSignInData"},
            {"id": "identity-user-profile", "name": "IdentityUserProfile", "method": "POST", "path": "/api/query/MobileBackend/IdentityUserProfile"},
        ],
        "client-push-notifications": [
            {"id": "add-notification-subscription", "name": "AddNotificationSubscription", "method": "POST", "path": "/api/publish/MobileBackend/AddNotificationSubscription"},
            {"id": "confirm-notification-delivery-v2", "name": "ConfirmNotificationDeliveryV2", "method": "POST", "path": "/api/publish/MobileBackend/ConfirmNotificationDeliveryV2"},
            {"id": "increase-document-stat-open", "name": "IncreaseDocumentStatOpen", "method": "POST", "path": "/api/publish/MobileBackend/IncreaseDocumentStatOpen"},
            {"id": "remove-notification-subscription", "name": "RemoveNotificationSubscription", "method": "POST", "path": "/api/publish/MobileBackend/RemoveNotificationSubscription"},
            {"id": "get-external-resource-v2", "name": "GetExternalResourceV2", "method": "POST", "path": "/api/query/MobileBackend/GetExternalResourceV2"},
            {"id": "get-icon-v2", "name": "GetIconV2", "method": "POST", "path": "/api/query/MobileBackend/GetIconV2"},
            {"id": "verify-notification-subscription", "name": "VerifyNotificationSubscription", "method": "POST", "path": "/api/query/MobileBackend/VerifyNotificationSubscription"},
        ],
        "client-user-management": [
            {"id": "create-or-update-identity-user-metadata", "name": "CreateOrUpdateIdentityUserMetadata", "method": "POST", "path": "/api/publish/MobileBackend/CreateOrUpdateIdentityUserMetadata"},
            {"id": "remove-identity-user", "name": "RemoveIdentityUser", "method": "POST", "path": "/api/publish/MobileBackend/RemoveIdentityUser"},
            {"id": "remove-identity-user-metadata", "name": "RemoveIdentityUserMetadata", "method": "POST", "path": "/api/publish/MobileBackend/RemoveIdentityUserMetadata"},
            {"id": "save-identity-user-activate-by-email", "name": "SaveIdentityUserActivateByEmail", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserActivateByEmail"},
            {"id": "save-identity-user-activate-by-email-with-password", "name": "SaveIdentityUserActivateByEmailWithPassword", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserActivateByEmailWithPassword"},
            {"id": "save-identity-user-reset-password", "name": "SaveIdentityUserResetPassword", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserResetPassword"},
            {"id": "save-identity-user-send-reset-password-email-anonymous", "name": "SaveIdentityUserSendResetPasswordEmailAnonymous", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserSendResetPasswordEmailAnonymous"},
            {"id": "save-identity-user-set-new-password", "name": "SaveIdentityUserSetNewPassword", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserSetNewPassword"},
            {"id": "save-identity-user-set-password-first-time", "name": "SaveIdentityUserSetPasswordFirstTime", "method": "POST", "path": "/api/publish/MobileBackend/SaveIdentityUserSetPasswordFirstTime"},
            {"id": "send-reset-password-email-by-email", "name": "SendResetPasswordEmailByEmail", "method": "POST", "path": "/api/publish/MobileBackend/SendResetPasswordEmailByEmail"},
            {"id": "get-identity-user-metadata", "name": "GetIdentityUserMetadata", "method": "POST", "path": "/api/query/MobileBackend/GetIdentityUserMetadata"},
        ],
        "client-other": [
            {"id": "add-mobile-error-entries", "name": "AddMobileErrorEntries", "method": "POST", "path": "/api/publish/MobileBackend/AddMobileErrorEntries"},
            {"id": "verify-debug-mode", "name": "VerifyDebugMode", "method": "POST", "path": "/api/query/MobileBackend/VerifyDebugMode"},
        ],
        "enterprise-client-management": [
            {"id": "add-users-to-groups", "name": "AddUsersToGroups", "method": "POST", "path": "/api/publish/MobileBackend/AddUsersToGroups"},
            {"id": "create-identity-users", "name": "CreateIdentityUsers", "method": "POST", "path": "/api/publish/MobileBackend/CreateIdentityUsers"},
            {"id": "create-or-update-identity-roles", "name": "CreateOrUpdateIdentityRoles", "method": "POST", "path": "/api/publish/MobileBackend/CreateOrUpdateIdentityRoles"},
            {"id": "create-or-update-identity-users", "name": "CreateOrUpdateIdentityUsers", "method": "POST", "path": "/api/publish/MobileBackend/CreateOrUpdateIdentityUsers"},
            {"id": "create-or-update-identity-users-metadata", "name": "CreateOrUpdateIdentityUsersMetadata", "method": "POST", "path": "/api/publish/MobileBackend/CreateOrUpdateIdentityUsersMetadata"},
            {"id": "create-or-update-identity-users-metadata-by-role", "name": "CreateOrUpdateIdentityUsersMetadataByRole", "method": "POST", "path": "/api/publish/MobileBackend/CreateOrUpdateIdentityUsersMetadataByRole"},
            {"id": "remove-identity-users-by-id", "name": "RemoveIdentityUsersById", "method": "POST", "path": "/api/publish/MobileBackend/RemoveIdentityUsersById"},
            {"id": "remove-identity-users-metadata", "name": "RemoveIdentityUsersMetadata", "method": "POST", "path": "/api/publish/MobileBackend/RemoveIdentityUsersMetadata"},
            {"id": "remove-identity-users-metadata-by-role", "name": "RemoveIdentityUsersMetadataByRole", "method": "POST", "path": "/api/publish/MobileBackend/RemoveIdentityUsersMetadataByRole"},
            {"id": "send-activation-mail-to-users", "name": "SendActivationMailToUsers", "method": "POST", "path": "/api/publish/MobileBackend/SendActivationMailToUsers"},
            {"id": "set-identity-user-password", "name": "SetIdentityUserPassword", "method": "POST", "path": "/api/publish/MobileBackend/SetIdentityUserPassword"},
            {"id": "update-identity-user", "name": "UpdateIdentityUser", "method": "POST", "path": "/api/publish/MobileBackend/UpdateIdentityUser"},
            {"id": "get-identity-batch-info", "name": "GetIdentityBatchInfo", "method": "POST", "path": "/api/query/MobileBackend/GetIdentityBatchInfo"},
            {"id": "list-identity-users-metadata", "name": "ListIdentityUsersMetadata", "method": "POST", "path": "/api/query/MobileBackend/ListIdentityUsersMetadata"},
            {"id": "list-user-by-date", "name": "ListUserByDate", "method": "POST", "path": "/api/query/MobileBackend/ListUserByDate"},
            {"id": "list-users-by-ids", "name": "ListUsersByIds", "method": "POST", "path": "/api/query/MobileBackend/ListUsersByIds"},
        ],
        "enterprise-content-delivery": [
            {"id": "content-delete", "name": "ContentDelete", "method": "POST", "path": "/api/publish/MobileBackend/ContentDelete"},
            {"id": "delete-content-by-date", "name": "DeleteContentByDate", "method": "POST", "path": "/api/publish/MobileBackend/DeleteContentByDate"},
            {"id": "delete-detached-documents-for-users", "name": "DeleteDetachedDocumentsForUsers", "method": "POST", "path": "/api/publish/MobileBackend/DeleteDetachedDocumentsForUsers"},
            {"id": "publish-app-template", "name": "PublishAppTemplate", "method": "POST", "path": "/api/publish/MobileBackend/PublishAppTemplate"},
            {"id": "content-list-with-filter-v4", "name": "ContentListWithFilterV4", "method": "POST", "path": "/api/query/MobileBackend/ContentListWithFilterV4"},
            {"id": "content-update-metadata-v4", "name": "ContentUpdateMetadataV4", "method": "POST", "path": "/api/query/MobileBackend/ContentUpdateMetadataV4"},
            {"id": "content-upload-v4", "name": "ContentUploadV4", "method": "POST", "path": "/api/query/MobileBackend/ContentUploadV4"},
        ],
        "enterprise-data-communication": [
            {"id": "multi-retrieve-data", "name": "MultiRetrieveData", "method": "POST", "path": "/api/longpoll/MobileBackend/MultiRetrieveData"},
            {"id": "retrieve-data", "name": "RetrieveData", "method": "POST", "path": "/api/longpoll/MobileBackend/RetrieveData"},
            {"id": "create-service-endpoint", "name": "CreateServiceEndpoint", "method": "POST", "path": "/api/publish/MobileBackend/CreateServiceEndpoint"},
            {"id": "delete-data", "name": "DeleteData", "method": "POST", "path": "/api/publish/MobileBackend/DeleteData"},
            {"id": "multi-store-reply-data", "name": "MultiStoreReplyData", "method": "POST", "path": "/api/publish/MobileBackend/MultiStoreReplyData"},
            {"id": "release-all-nodes-data", "name": "ReleaseAllNodesData", "method": "POST", "path": "/api/publish/MobileBackend/ReleaseAllNodesData"},
            {"id": "release-node-data", "name": "ReleaseNodeData", "method": "POST", "path": "/api/publish/MobileBackend/ReleaseNodeData"},
            {"id": "store-reply-data", "name": "StoreReplyData", "method": "POST", "path": "/api/publish/MobileBackend/StoreReplyData"},
            {"id": "transfer-node-data", "name": "TransferNodeData", "method": "POST", "path": "/api/publish/MobileBackend/TransferNodeData"},
            {"id": "get-channel-data", "name": "GetChannelData", "method": "POST", "path": "/api/query/MobileBackend/GetChannelData"},
            {"id": "list-channel-usage-info", "name": "ListChannelUsageInfo", "method": "POST", "path": "/api/query/MobileBackend/ListChannelUsageInfo"},
        ],
        "enterprise-dc-states": [
            {"id": "assign-dc-state-to-client", "name": "AssignDcStateToClient", "method": "POST", "path": "/api/publish/MobileBackend/AssignDcStateToClient"},
            {"id": "delete-dc-states-by-date", "name": "DeleteDcStatesByDate", "method": "POST", "path": "/api/publish/MobileBackend/DeleteDcStatesByDate"},
            {"id": "delete-dc-states-by-ids", "name": "DeleteDcStatesByIds", "method": "POST", "path": "/api/publish/MobileBackend/DeleteDcStatesByIds"},
            {"id": "get-client-dc-state", "name": "GetClientDcState", "method": "POST", "path": "/api/query/MobileBackend/GetClientDcState"},
            {"id": "list-application-dc-states", "name": "ListApplicationDcStates", "method": "POST", "path": "/api/query/MobileBackend/ListApplicationDcStates"},
            {"id": "list-client-dc-states", "name": "ListClientDcStates", "method": "POST", "path": "/api/query/MobileBackend/ListClientDcStates"},
        ],
        "enterprise-other": [
            {"id": "create-external-token-verified-access-token", "name": "CreateExternalTokenVerifiedAccessToken", "method": "POST", "path": "/api/publish/MobileBackend/CreateExternalTokenVerifiedAccessToken"},
            {"id": "create-server-authenticated-access-token", "name": "CreateServerAuthenticatedAccessToken", "method": "POST", "path": "/api/publish/MobileBackend/CreateServerAuthenticatedAccessToken"},
            {"id": "import-application-package", "name": "ImportApplicationPackage", "method": "POST", "path": "/api/publish/MobileBackend/ImportApplicationPackage"},
            {"id": "import-build-package", "name": "ImportBuildPackage", "method": "POST", "path": "/api/publish/MobileBackend/ImportBuildPackage"},
            {"id": "remove-client-notification-subscriptions", "name": "RemoveClientNotificationSubscriptions", "method": "POST", "path": "/api/publish/MobileBackend/RemoveClientNotificationSubscriptions"},
            {"id": "revoke-server-authenticated-access-token", "name": "RevokeServerAuthenticatedAccessToken", "method": "POST", "path": "/api/publish/MobileBackend/RevokeServerAuthenticatedAccessToken"},
            {"id": "send-notifications", "name": "SendNotifications", "method": "POST", "path": "/api/publish/MobileBackend/SendNotifications"},
            {"id": "send-notifications-to-device", "name": "SendNotificationsToDevice", "method": "POST", "path": "/api/publish/MobileBackend/SendNotificationsToDevice"},
            {"id": "export-application-package", "name": "ExportApplicationPackage", "method": "POST", "path": "/api/query/MobileBackend/ExportApplicationPackage"},
            {"id": "export-build-package", "name": "ExportBuildPackage", "method": "POST", "path": "/api/query/MobileBackend/ExportBuildPackage"},
            {"id": "get-notification-raw-data", "name": "GetNotificationRawData", "method": "POST", "path": "/api/query/MobileBackend/GetNotificationRawData"},
            {"id": "verify-api-key", "name": "VerifyApiKey", "method": "POST", "path": "/api/query/MobileBackend/VerifyApiKey"},
            {"id": "verify-service", "name": "VerifyService", "method": "POST", "path": "/api/query/MobileBackend/VerifyService"},
            {"id": "digital-advantage-suite-package-file", "name": "DigitalAdvantageSuitePackageFile", "method": "POST", "path": "/api/upload/MobileBackend/DigitalAdvantageSuitePackageFile"},
        ],
        "server-availability": [
            {"id": "ping", "name": "Ping", "method": "POST", "path": "/api/query/MobileBackend/Ping"},
        ]
    }
    
    # Return endpoints for category or empty list if category doesn't exist
    return endpoints_map.get(category_id, [])

def endpoint_detail(request, endpoint_id):
    """View for displaying and testing a specific endpoint"""
    # Map endpoint IDs to full endpoint details
    all_endpoints = {}
    # Fill all_endpoints by getting all endpoints from all categories
    for category_id in ["client-content-delivery", "client-data-communication", "client-dc-states", 
                        "client-identity-providers", "client-push-notifications", "client-user-management",
                        "client-other", "enterprise-client-management", "enterprise-content-delivery",
                        "enterprise-data-communication", "enterprise-dc-states", "enterprise-other",
                        "server-availability"]:
        category_endpoints = get_endpoints_for_category(category_id)
        for endpoint in category_endpoints:
            all_endpoints[endpoint['id']] = endpoint
    
    endpoint = all_endpoints.get(endpoint_id)
    if not endpoint:
        return JsonResponse({"error": "Endpoint not found"}, status=404)
    
    return render(request, 'api_client/endpoint_detail.html', {
        'endpoint': endpoint
    })

@csrf_exempt
def call_api(request):
    """View for making API calls and returning the results"""
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
    try:
        data = json.loads(request.body)
        endpoint_path = data.get('path')
        request_data = data.get('data', {})
        
        # Make API call
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            f"{API_BASE_URL}{endpoint_path}",
            headers=headers,
            json=request_data
        )
        
        # Try to parse response as JSON
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            # Return raw response if not JSON
            response_data = {"raw_response": response.text}
        
        return JsonResponse({
            "status_code": response.status_code,
            "response": response_data
        })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

def report_query(request):
    """View for querying and displaying Messenger reports"""
    import requests
    import csv
    from io import StringIO
    from .services import QuadientAPIClient
    
    error_message = None
    report_content = None
    filename = None
    batch_id = None
    status_code = None
    
    if request.method == "POST":
        batch_id = request.POST.get('batch_id')
        if batch_id:
            try:
                # Get the API client instance
                client = QuadientAPIClient()
                
                # Setup the request
                url = f"{client.base_url}/api/query/Messenger/ReportQuery"
                data = {"batchId": int(batch_id)}
                
                # Add required headers
                headers = client.headers.copy()
                headers['User-Agent'] = 'EPPS d.o.o./MessengerStater'
                
                # Make the request
                response = requests.post(
                    url,
                    headers=headers,
                    json=data
                )
                
                # Log the request
                client._log_request(
                    endpoint="/api/query/Messenger/ReportQuery",
                    method="POST",
                    request_data=data,
                    response=response
                )
                
                # Process the response
                status_code = response.status_code
                if response.status_code == 200:
                    report_content = response.text
                    if 'Content-Disposition' in response.headers:
                        filename = response.headers['Content-Disposition'].split("=")[1].replace('"', '')
                else:
                    error_message = f"Failed to fetch report. Status code: {response.status_code}"
            except Exception as e:
                error_message = f"Error processing request: {str(e)}"
        else:
            error_message = "Batch ID is required"
    
    # Parse the data if available
    parsed_data = {
        'messages': [],
        'trackurls': [],
        'stats': {
            'total_messages': 0,
            'total_opened': 0,
            'total_clicked': 0,
            'unique_recipients': set(),
            'providers': {}
        }
    }
    
    if report_content:
        # Detect the format (tab-delimited or CSV with semicolons)
        if '\t' in report_content[:100]:
            # Tab-delimited format
            lines = report_content.strip().split('\n')
            for line in lines:
                fields = line.split('\t')
                if fields and len(fields) > 5:
                    process_record(fields, parsed_data)
        else:
            # CSV format with semicolons as delimiters
            csv_reader = csv.reader(
                StringIO(report_content), 
                delimiter=';', 
                quotechar='"'
            )
            for fields in csv_reader:
                if fields and len(fields) > 5:
                    process_record(fields, parsed_data)
    
    # Convert set to count for unique recipients
    if 'unique_recipients' in parsed_data['stats']:
        parsed_data['stats']['unique_recipient_count'] = len(parsed_data['stats']['unique_recipients'])
        # Remove the set as it's not JSON serializable
        del parsed_data['stats']['unique_recipients']
    
    # Calculate open and click rates
    if parsed_data['stats']['total_messages'] > 0:
        parsed_data['stats']['open_rate'] = round(
            (parsed_data['stats']['total_opened'] / parsed_data['stats']['total_messages']) * 100, 2
        )
        parsed_data['stats']['click_rate'] = round(
            (parsed_data['stats']['total_clicked'] / parsed_data['stats']['total_messages']) * 100, 2
        )
    else:
        parsed_data['stats']['open_rate'] = 0
        parsed_data['stats']['click_rate'] = 0
    
    return render(request, 'api_client/report_query.html', {
        'error_message': error_message,
        'report_content': report_content,
        'filename': filename,
        'batch_id': batch_id,
        'status_code': status_code,
        'parsed_data': parsed_data
    })

def process_record(fields, parsed_data):
    """Process a record from the report data"""
    record_type = fields[0].strip('"')
    
    if record_type == 'Message':
        # Process message record
        opens = int(fields[8].strip('"')) if len(fields) > 8 and fields[8].strip('"').isdigit() else 0
        clicks = int(fields[9].strip('"')) if len(fields) > 9 and fields[9].strip('"').isdigit() else 0
        provider = fields[10].strip('"') if len(fields) > 10 else ''
        
        # Extract sender if available (in the expanded format)
        sender = fields[16].strip('"') if len(fields) > 16 else ''
        sent_time = fields[18].strip('"') if len(fields) > 18 else ''
        
        message = {
            'number': fields[1].strip('"') if len(fields) > 1 else '',
            'email': fields[2].strip('"') if len(fields) > 2 else '',
            'status': fields[3].strip('"') if len(fields) > 3 else '',
            'status_code': fields[4].strip('"') if len(fields) > 4 else '',
            'detail': fields[5].strip('"') if len(fields) > 5 else '',
            'open_time': fields[6].strip('"') if len(fields) > 6 and fields[6].strip('"') else '',
            'click_time': fields[7].strip('"') if len(fields) > 7 and fields[7].strip('"') else '',
            'opens': opens,
            'clicks': clicks,
            'provider': provider,
            'id': fields[11].strip('"') if len(fields) > 11 else '',
            'landing_page_url': fields[12].strip('"') if len(fields) > 12 else '',
            'sender': sender,
            'sent_time': sent_time
        }
        
        # Update statistics
        parsed_data['stats']['total_messages'] += 1
        if opens > 0:
            parsed_data['stats']['total_opened'] += 1
        if clicks > 0:
            parsed_data['stats']['total_clicked'] += 1
        
        email = fields[2].strip('"') if len(fields) > 2 else ''
        if email:
            parsed_data['stats']['unique_recipients'].add(email)
        
        if provider:
            if provider in parsed_data['stats']['providers']:
                parsed_data['stats']['providers'][provider] += 1
            else:
                parsed_data['stats']['providers'][provider] = 1
        
        parsed_data['messages'].append(message)
        
    elif record_type == 'TrackUrl':
        # Process TrackUrl record
        trackurl = {
            'url': fields[1].strip('"') if len(fields) > 1 else '',
            'timestamp': fields[2].strip('"') if len(fields) > 2 else '',
            'ip': fields[3].strip('"') if len(fields) > 3 else ''
        }
        parsed_data['trackurls'].append(trackurl)



def batch_list(request):
    """View for listing batches from Quadient API"""
    import requests
    from datetime import datetime, timedelta
    from django.shortcuts import render
    from .services import QuadientAPIClient
    
    error_message = None
    batches = {
        'running': [],
        'waiting': [],
        'onDemand': []
    }
    batch_count = 0
    
    # Default to last 30 days if no date parameters provided
    default_from = datetime.now() - timedelta(days=30)
    default_to = datetime.now()
    
    # Process form submission
    if request.method == "POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        batch_type = request.POST.get('batch_type')
        
        try:
            # Get the API client instance
            client = QuadientAPIClient()
            
            # Setup the request to get batches
            url = f"{client.base_url}/api/query/Messenger/ListBatchesQueryByUploadTimeV2"
            
            # Convert dates to ISO format
            from_datetime = datetime.fromisoformat(from_date) if from_date else default_from
            to_datetime = datetime.fromisoformat(to_date) if to_date else default_to
            
            # Prepare request data
            data = {
                "from": from_datetime.isoformat(),
                "to": to_datetime.isoformat()
            }
            
            # Add batch type if specified
            if batch_type and batch_type != "All":
                data["type"] = batch_type
            
            print(data)
            # Make the request
            response = requests.post(
                url,
                headers=client.headers,
                json=data
            )
         
            # Log the request
            client._log_request(
                endpoint="/api/query/Messenger/ListBatchesQueryByUploadTimeV2",
                method="POST",
                request_data=data,
                response=response
            )
            
            # Process the response
            if response.status_code == 200:
                result = response.json()
                
                # Extract batch data from response
                batches = {
                    'running': result.get('running', []),
                    'waiting': result.get('waiting', []),
                    'onDemand': result.get('onDemand', [])
                }
                
                # Calculate total batch count
                batch_count = (
                    len(batches['running']) + 
                    len(batches['waiting']) + 
                    len(batches['onDemand'])
                )
            else:
                error_message = f"Failed to fetch batches. Status code: {response.status_code}"
        except Exception as e:
            error_message = f"Error processing request: {str(e)}"
    
    # Default values for the form
    context = {
        'error_message': error_message,
        'batches': batches,
        'batch_count': batch_count,
        'from_date': default_from.strftime('%Y-%m-%d'),
        'to_date': default_to.strftime('%Y-%m-%d'),
        'batch_types': [
            {'value': 'All', 'label': 'All Types'},
            {'value': 'Email', 'label': 'Email'},
            {'value': 'Sms', 'label': 'SMS'},
            {'value': 'WhatsApp', 'label': 'WhatsApp'},
            {'value': 'Notification', 'label': 'Notification'},
            {'value': 'DocumentUpdate', 'label': 'Document Update'},
            {'value': 'AppTemplateUpdate', 'label': 'App Template Update'}
        ],
        'selected_type': request.POST.get('batch_type', 'All')
    }
    
    return render(request, 'api_client/batch_list.html', context)


def batch_device_analytics(request):
    """API endpoint for device and client analytics for a specific batch"""
    import json
    from django.http import JsonResponse
    from datetime import datetime, timedelta
    from .services import QuadientAPIClient
    
    # Get batch ID from request
    batch_id = request.GET.get('batch_id')
    
    if not batch_id:
        return JsonResponse({
            'success': False,
            'error': 'Batch ID is required'
        }, status=400)
    
    try:
        # Get the API client instance
        client = QuadientAPIClient()
        
        # Get batch details first to ensure it exists
        batch_details_response = client.make_request(
            endpoint="/api/query/Messenger/ContentListWithFilterV4",
            method="POST",
            data={
                "filter": {
                    "documentIds": [int(batch_id)]
                }
            }
        )
        
        if not batch_details_response or batch_details_response.status_code != 200:
            return JsonResponse({
                'success': False,
                'error': 'Failed to retrieve batch details'
            }, status=500)
        
        batch_details = batch_details_response.json()
        if not batch_details.get('documents'):
            return JsonResponse({
                'success': False,
                'error': 'Batch not found'
            }, status=404)
        
        # Get device and client statistics for the batch
        stats_response = client.make_request(
            endpoint="/api/query/Messenger/BatchStatisticsByBatchIds",
            method="POST",
            data={"batchIds": [int(batch_id)]}
        )
        
        if not stats_response or stats_response.status_code != 200:
            return JsonResponse({
                'success': False,
                'error': 'Failed to retrieve batch statistics'
            }, status=500)
        
        stats_data = stats_response.json()
        
        # Extract OS and browser statistics
        os_stats = {}
        browser_stats = {}
        
        # Process client OS data
        if 'clientOS' in stats_data:
            # Convert array to dictionary if it's an array of objects
            if isinstance(stats_data['clientOS'], list):
                for item in stats_data['clientOS']:
                    if isinstance(item, dict) and 'key' in item and 'value' in item:
                        os_name = clean_os_name(item['key'])
                        os_stats[os_name] = item['value']
            # If it's already a dictionary, use it directly
            elif isinstance(stats_data['clientOS'], dict):
                for key, value in stats_data['clientOS'].items():
                    os_name = clean_os_name(key)
                    os_stats[os_name] = value
        
        # Process client browser data
        if 'clientBrowser' in stats_data:
            # Convert array to dictionary if it's an array of objects
            if isinstance(stats_data['clientBrowser'], list):
                for item in stats_data['clientBrowser']:
                    if isinstance(item, dict) and 'key' in item and 'value' in item:
                        browser_name = clean_browser_name(item['key'])
                        browser_stats[browser_name] = item['value']
            # If it's already a dictionary, use it directly
            elif isinstance(stats_data['clientBrowser'], dict):
                for key, value in stats_data['clientBrowser'].items():
                    browser_name = clean_browser_name(key)
                    browser_stats[browser_name] = value
        
        # Get batch report for detailed metrics
        report_response = client.make_request(
            endpoint="/api/query/Messenger/ReportQuery",
            method="POST",
            data={"batchId": int(batch_id)}
        )
        
        # Initialize time-based engagement data
        hourly_engagement = {}
        day_of_week_engagement = {}
        
        # Initialize total metrics
        total_opens = sum(os_stats.values())
        total_clicks = 0
        total_sent = 0
        total_delivered = 0
        
        # Get batch details from the list endpoint
        batch_data = batch_details.get('documents', [])[0] if batch_details.get('documents') else {}
        total_sent = batch_data.get('sent', 0)
        total_delivered = batch_data.get('delivered', 0)
        
        # Calculate device categories
        device_categories = {
            'Desktop': 0,
            'Mobile': 0,
            'Tablet': 0,
            'Other': 0
        }
        
        # Maps of OS names to device categories
        os_device_map = {
            'Windows': 'Desktop',
            'MacOS': 'Desktop',
            'Linux': 'Desktop',
            'iOS': 'Mobile',
            'Android': 'Mobile',
            'ChromeOS': 'Desktop',
            'WindowsPhone': 'Mobile',
            'BlackBerry': 'Mobile'
        }
        
        # Calculate device categories from OS data
        for os_name, count in os_stats.items():
            category = os_device_map.get(os_name, 'Other')
            device_categories[category] += count
        
        # Email client categories
        email_client_categories = {
            'Webmail': 0,
            'Desktop Client': 0,
            'Mobile Client': 0,
            'Other': 0
        }
        
        # Maps of browser names to email client categories
        browser_client_map = {
            'Gmail': 'Webmail',
            'Outlook': 'Desktop Client',
            'AppleMail': 'Desktop Client',
            'Thunderbird': 'Desktop Client',
            'WindowsLiveMail': 'Desktop Client',
            'Chrome': 'Webmail',
            'Firefox': 'Webmail',
            'Safari': 'Webmail',
            'Edge': 'Webmail',
            'ChromeMobile': 'Mobile Client',
            'FirefoxMobile': 'Mobile Client',
            'SafariMobile': 'Mobile Client',
            'EdgeMobile': 'Mobile Client'
        }
        
        # Calculate email client categories from browser data
        for browser_name, count in browser_stats.items():
            category = browser_client_map.get(browser_name, 'Other')
            email_client_categories[category] += count
        
        # Return the data
        return JsonResponse({
            'success': True,
            'batch_id': batch_id,
            'batch_name': batch_data.get('name', f'Batch {batch_id}'),
            'batch_type': batch_data.get('type', 'Unknown'),
            'total_sent': total_sent,
            'total_delivered': total_delivered,
            'total_opens': total_opens,
            'total_clicks': batch_data.get('uniqueClicks', 0),
            'os_stats': os_stats,
            'browser_stats': browser_stats,
            'device_categories': device_categories,
            'email_client_categories': email_client_categories
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

def clean_os_name(os_name):
    """Clean and normalize OS names"""
    # Remove NotOpenedYet or Unknown
    if os_name in ['NotOpenedYet', 'Unknown']:
        return 'Unknown'
    
    # Simplify Windows versions
    if os_name.startswith('Windows'):
        return 'Windows'
    
    # Simplify MacOS versions
    if os_name.startswith('MacOSX'):
        return 'MacOS'
    
    # Simplify Android versions
    if os_name.startswith('Android'):
        return 'Android'
    
    # Simplify iOS versions
    if os_name.startswith('iOS'):
        return 'iOS'
    
    return os_name

def clean_browser_name(browser_name):
    """Clean and normalize browser names"""
    # Remove NotOpenedYet or Unknown
    if browser_name in ['NotOpenedYet', 'Unknown']:
        return 'Unknown'
    
    # Normalize Chrome variants
    if browser_name in ['Chrome', 'ChromeMobile', 'ChromeMobileIos']:
        return 'Chrome'
    
    # Normalize Firefox variants
    if browser_name in ['Firefox', 'FirefoxMobile', 'FirefoxIos']:
        return 'Firefox'
    
    # Normalize Safari variants
    if browser_name in ['Safari', 'SafariMobile', 'SafariMobileWebView']:
        return 'Safari'
    
    # Normalize Edge variants
    if browser_name in ['Edge', 'EdgeMobile']:
        return 'Edge'
    
    # Normalize Outlook variants
    if browser_name.startswith('Outlook'):
        return 'Outlook'
    
    return browser_name



def time_analytics(request):
    """API endpoint for time-based analytics"""
    import json
    from django.http import JsonResponse
    from datetime import datetime, timedelta
    import re
    from .services import QuadientAPIClient
    
    # Get date range from request
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    
    # Default to last 30 days if not provided
    if not from_date:
        from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    if not to_date:
        to_date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        # Convert string dates to datetime objects
        from_datetime = datetime.fromisoformat(from_date)
        to_datetime = datetime.fromisoformat(to_date)
        
        # Get the API client instance
        client = QuadientAPIClient()
        
        # Query batches for the date range
        batches_response = client.make_request(
            endpoint="/api/query/Messenger/ListBatchesQueryByUploadTimeV2",
            method="POST",
            data={
                "from": from_datetime.isoformat(),
                "to": to_datetime.isoformat()
            }
        )
        
        if not batches_response or batches_response.status_code != 200:
            return JsonResponse({
                'success': False,
                'error': 'Failed to retrieve batch data'
            }, status=500)
        
        batch_data = batches_response.json()
        
        # Combine all batches
        all_batches = []
        for category in ['running', 'waiting', 'onDemand']:
            if category in batch_data:
                all_batches.extend(batch_data[category])
        
        # Get the most recent 5 completed batches to analyze
        completed_batches = [b for b in all_batches if b.get('state') == 'Completed']
        completed_batches.sort(key=lambda x: x.get('lastUploadTime', '/Date(0)/'), reverse=True)
        recent_batches = completed_batches[:5]
        
        # Initialize time-based data structures
        hours_of_day = [f"{i:02d}:00" for i in range(24)]
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Initialize heatmap data structures
        hourly_heatmap = {hour: {'opens': 0, 'clicks': 0} for hour in hours_of_day}
        daily_heatmap = {day: {'opens': 0, 'clicks': 0} for day in days_of_week}
        
        # Track total opens and clicks
        total_opens = 0
        total_clicks = 0
        
        # Process batches to get time-based data
        for batch in recent_batches:
            batch_id = batch.get('id')
            
            if not batch_id:
                continue
            
            # Get report for this batch
            report_response = client.make_request(
                endpoint="/api/query/Messenger/ReportQuery",
                method="POST",
                data={"batchId": batch_id}
            )
            
            if not report_response or report_response.status_code != 200:
                continue
            
            # Parse the report data for opens and clicks
            report_text = report_response.content.decode('utf-8')
            
            # Process report data line by line
            for line in report_text.split('\n'):
                # Check if this is a Message line with opens or clicks
                if line.startswith('Message') and '\t' in line:
                    fields = line.split('\t')
                    
                    # Check if we have enough fields and there are opens or clicks
                    if len(fields) >= 10:
                        # Look for open time
                        open_time = fields[6] if len(fields) > 6 and fields[6] else None
                        click_time = fields[7] if len(fields) > 7 and fields[7] else None
                        
                        # Process open time
                        if open_time:
                            try:
                                # Parse datetime
                                open_dt = datetime.fromisoformat(open_time.replace('Z', '+00:00'))
                                
                                # Extract hour and day of week
                                hour = open_dt.strftime('%H:00')
                                day = open_dt.strftime('%A')
                                
                                # Increment counters
                                hourly_heatmap[hour]['opens'] += 1
                                daily_heatmap[day]['opens'] += 1
                                total_opens += 1
                            except (ValueError, TypeError):
                                pass
                        
                        # Process click time
                        if click_time:
                            try:
                                # Parse datetime
                                click_dt = datetime.fromisoformat(click_time.replace('Z', '+00:00'))
                                
                                # Extract hour and day of week
                                hour = click_dt.strftime('%H:00')
                                day = click_dt.strftime('%A')
                                
                                # Increment counters
                                hourly_heatmap[hour]['clicks'] += 1
                                daily_heatmap[day]['clicks'] += 1
                                total_clicks += 1
                            except (ValueError, TypeError):
                                pass
                
                # Look for TrackUrl lines which indicate clicks
                if line.startswith('TrackUrl') and '\t' in line:
                    fields = line.split('\t')
                    
                    # Check if we have enough fields and there is a timestamp
                    if len(fields) >= 3:
                        track_time = fields[2] if len(fields) > 2 and fields[2] else None
                        
                        # Process track time
                        if track_time:
                            try:
                                # Parse datetime
                                track_dt = datetime.fromisoformat(track_time.replace('Z', '+00:00'))
                                
                                # Extract hour and day of week
                                hour = track_dt.strftime('%H:00')
                                day = track_dt.strftime('%A')
                                
                                # Increment counters - we already counted these in the Message processing,
                                # so we don't increment total_clicks again
                                hourly_heatmap[hour]['clicks'] += 1
                                daily_heatmap[day]['clicks'] += 1
                            except (ValueError, TypeError):
                                pass
        
        # Find optimal sending times based on open rates
        sorted_hours = sorted(hourly_heatmap.items(), key=lambda x: x[1]['opens'], reverse=True)
        optimal_hours = [hour for hour, _ in sorted_hours[:3]]
        
        sorted_days = sorted(daily_heatmap.items(), key=lambda x: x[1]['opens'], reverse=True)
        optimal_days = [day for day, _ in sorted_days[:3]]
        
        # Format heatmap data for visualization
        hourly_data = []
        for hour, counts in hourly_heatmap.items():
            hourly_data.append({
                'hour': hour,
                'opens': counts['opens'],
                'clicks': counts['clicks']
            })
        
        daily_data = []
        for day, counts in daily_heatmap.items():
            daily_data.append({
                'day': day,
                'opens': counts['opens'],
                'clicks': counts['clicks']
            })
        
        # Return the data
        return JsonResponse({
            'success': True,
            'total_opens': total_opens,
            'total_clicks': total_clicks,
            'optimal_hours': optimal_hours,
            'optimal_days': optimal_days,
            'hourly_data': hourly_data,
            'daily_data': daily_data
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
    


def compliance_monitoring(request):
    """API endpoint for compliance and unsubscribe monitoring"""
    import json
    from django.http import JsonResponse
    from datetime import datetime, timedelta
    from .services import QuadientAPIClient
    from collections import defaultdict
    
    # Get date range from request
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    
    # Default to last 30 days if not provided
    if not from_date:
        from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    if not to_date:
        to_date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        # Convert string dates to datetime objects
        from_datetime = datetime.fromisoformat(from_date)
        to_datetime = datetime.fromisoformat(to_date)
        
        # Get the API client instance
        client = QuadientAPIClient()
        
        # Query batches for the date range
        batches_response = client.make_request(
            endpoint="/api/query/Messenger/ListBatchesQueryByUploadTimeV2",
            method="POST",
            data={
                "from": from_datetime.isoformat(),
                "to": to_datetime.isoformat()
            }
        )
        
        if not batches_response or batches_response.status_code != 200:
            return JsonResponse({
                'success': False,
                'error': 'Failed to retrieve batch data'
            }, status=500)
        
        batch_data = batches_response.json()
        
        # Combine all batches
        all_batches = []
        for category in ['running', 'waiting', 'onDemand']:
            if category in batch_data:
                all_batches.extend(batch_data[category])
        
        # If no batches, return empty data
        if not all_batches:
            return JsonResponse({
                'success': True,
                'total_sent': 0,
                'total_unsubscribed': 0,
                'total_spam_complaints': 0,
                'unsubscribe_rate': 0,
                'spam_complaint_rate': 0,
                'batches': [],
                'trends': {
                    'dates': [],
                    'unsubscribe_rates': [],
                    'spam_complaint_rates': []
                }
            })
        
        # Sort batches by upload time
        all_batches.sort(key=lambda x: x.get('lastUploadTime', '/Date(0)/'))
        
        # Initialize counters
        total_sent = 0
        total_unsubscribed = 0
        total_spam_complaints = 0
        
        # Initialize data for trends
        dates = []
        unsubscribe_counts = []
        spam_complaint_counts = []
        
        # Process each batch
        batch_compliance_data = []
        daily_unsubscribes = defaultdict(int)
        daily_spam_complaints = defaultdict(int)
        daily_sent = defaultdict(int)
        
        for batch in all_batches:
            batch_id = batch.get('id')
            batch_name = batch.get('name', f'Batch {batch_id}')
            batch_sent = batch.get('sent', 0)
            batch_unsubscribed = batch.get('unsubscribeCount', 0)
            batch_spam = batch.get('markedAsSpam', 0)
            batch_date = None
            
            # Extract date from lastUploadTime
            if 'lastUploadTime' in batch:
                try:
                    timestamp_str = batch['lastUploadTime']
                    timestamp = int(timestamp_str.replace('/Date(', '').replace(')/', '')) / 1000
                    batch_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                except (ValueError, TypeError):
                    batch_date = None
            
            # Skip if no date or sent count
            if not batch_date or batch_sent == 0:
                continue
            
            # Update daily totals
            daily_sent[batch_date] += batch_sent
            daily_unsubscribes[batch_date] += batch_unsubscribed
            daily_spam_complaints[batch_date] += batch_spam
            
            # Calculate rates
            unsubscribe_rate = (batch_unsubscribed / batch_sent) * 100 if batch_sent > 0 else 0
            spam_rate = (batch_spam / batch_sent) * 100 if batch_sent > 0 else 0
            
            # Determine if there are unusual spikes (rates significantly higher than average)
            is_unsubscribe_spike = unsubscribe_rate > 1.0  # More than 1% is considered high
            is_spam_spike = spam_rate > 0.1  # More than 0.1% is considered high
            
            # Add batch data
            batch_compliance_data.append({
                'batch_id': batch_id,
                'batch_name': batch_name,
                'date': batch_date,
                'sent': batch_sent,
                'unsubscribed': batch_unsubscribed,
                'spam_complaints': batch_spam,
                'unsubscribe_rate': round(unsubscribe_rate, 2),
                'spam_rate': round(spam_rate, 2),
                'is_unsubscribe_spike': is_unsubscribe_spike,
                'is_spam_spike': is_spam_spike
            })
            
            # Update totals
            total_sent += batch_sent
            total_unsubscribed += batch_unsubscribed
            total_spam_complaints += batch_spam
        
        # Calculate overall rates
        unsubscribe_rate = (total_unsubscribed / total_sent) * 100 if total_sent > 0 else 0
        spam_complaint_rate = (total_spam_complaints / total_sent) * 100 if total_sent > 0 else 0
        
        # Get all dates in the range
        date_range = []
        current_date = from_datetime
        while current_date <= to_datetime:
            date_str = current_date.strftime('%Y-%m-%d')
            date_range.append(date_str)
            
            # If we have data for this date, add it to the trends
            if date_str in daily_sent and daily_sent[date_str] > 0:
                dates.append(date_str)
                daily_unsub_rate = (daily_unsubscribes[date_str] / daily_sent[date_str]) * 100
                daily_spam_rate = (daily_spam_complaints[date_str] / daily_sent[date_str]) * 100
                unsubscribe_counts.append(round(daily_unsub_rate, 2))
                spam_complaint_counts.append(round(daily_spam_rate, 2))
            
            current_date += timedelta(days=1)
        
        # Return the data
        return JsonResponse({
            'success': True,
            'total_sent': total_sent,
            'total_unsubscribed': total_unsubscribed,
            'total_spam_complaints': total_spam_complaints,
            'unsubscribe_rate': round(unsubscribe_rate, 2),
            'spam_complaint_rate': round(spam_complaint_rate, 2),
            'batches': batch_compliance_data,
            'trends': {
                'dates': dates,
                'unsubscribe_rates': unsubscribe_counts,
                'spam_complaint_rates': spam_complaint_counts
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

def batch_compliance_data(request):
    """API endpoint for compliance data for a specific batch"""
    import json
    from django.http import JsonResponse
    from .services import QuadientAPIClient
    from datetime import datetime
    
    # Get batch ID from request
    batch_id = request.GET.get('batch_id')
    
    if not batch_id:
        return JsonResponse({
            'success': False,
            'error': 'Batch ID is required'
        }, status=400)
    
    try:
        # Get the API client instance
        client = QuadientAPIClient()
        
        # Get batch details
        batch_details_response = client.make_request(
            endpoint="/api/query/Messenger/ContentListWithFilterV4",
            method="POST",
            data={
                "filter": {
                    "documentIds": [int(batch_id)]
                }
            }
        )
        
        if not batch_details_response or batch_details_response.status_code != 200:
            return JsonResponse({
                'success': False,
                'error': 'Failed to retrieve batch details'
            }, status=500)
        
        batch_details = batch_details_response.json()
        if not batch_details.get('documents'):
            return JsonResponse({
                'success': False,
                'error': 'Batch not found'
            }, status=404)
        
        batch_data = batch_details.get('documents', [])[0]
        
        # Extract compliance metrics
        batch_sent = batch_data.get('sent', 0)
        batch_unsubscribed = batch_data.get('unsubscribeCount', 0)
        batch_spam = batch_data.get('markedAsSpam', 0)
        
        # Calculate rates
        unsubscribe_rate = (batch_unsubscribed / batch_sent) * 100 if batch_sent > 0 else 0
        spam_rate = (batch_spam / batch_sent) * 100 if batch_sent > 0 else 0
        
        # Determine if there are unusual spikes
        is_unsubscribe_spike = unsubscribe_rate > 1.0  # More than 1% is considered high
        is_spam_spike = spam_rate > 0.1  # More than 0.1% is considered high
        
        # Extract unsubscribe details if available
        unsubscribed_recipients = []
        
        # Get report for this batch to extract unsubscribe details
        report_response = client.make_request(
            endpoint="/api/query/Messenger/ReportQuery",
            method="POST",
            data={"batchId": int(batch_id)}
        )
        
        if report_response and report_response.status_code == 200:
            # Parse the report data for unsubscribes
            report_text = report_response.content.decode('utf-8')
            
            # Process report data line by line
            for line in report_text.split('\n'):
                # Check if this is a Message line with unsubscribe status
                if line.startswith('Message') and '\t' in line:
                    fields = line.split('\t')
                    
                    # Check if we have enough fields and unsubscribe status
                    if len(fields) >= 10:
                        # Recipient email
                        email = fields[2] if len(fields) > 2 else ''
                        # Unsubscribe status - looking for 'true' in the unsubscribed field
                        unsubscribed = fields[11] if len(fields) > 11 and fields[11].lower() == 'true' else False
                        
                        if email and unsubscribed:
                            unsubscribed_recipients.append(email)
        
        # Return the data
        return JsonResponse({
            'success': True,
            'batch_id': int(batch_id),
            'batch_name': batch_data.get('name', f'Batch {batch_id}'),
            'sent': batch_sent,
            'unsubscribed': batch_unsubscribed,
            'spam_complaints': batch_spam,
            'unsubscribe_rate': round(unsubscribe_rate, 2),
            'spam_rate': round(spam_rate, 2),
            'is_unsubscribe_spike': is_unsubscribe_spike,
            'is_spam_spike': is_spam_spike,
            'unsubscribed_recipients': unsubscribed_recipients
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
    



def start_batch(request):
    """API endpoint to start sending a batch"""
    import json
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from .services import QuadientAPIClient
    
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        batch_id = data.get('batchId')
        
        if not batch_id:
            return JsonResponse({'success': False, 'error': 'Batch ID is required'}, status=400)
        
        # Get the API client instance
        client = QuadientAPIClient()
        
        # Call the StartBatchSending API
        url = f"{client.base_url}/api/publish/Messenger/StartBatchSending"
        request_data = {"batchId": batch_id}
        
        response = client.make_request(
            endpoint="/api/publish/Messenger/StartBatchSending",
            method="POST",
            data=request_data
        )
        
        if response and response.status_code == 200:
            return JsonResponse({'success': True})
        else:
            error_message = "Failed to start batch"
            if response:
                try:
                    result = response.json()
                    if 'error' in result and result['error']:
                        error_message = result['error'].get('error', error_message)
                except:
                    pass
            
            return JsonResponse({'success': False, 'error': error_message}, status=400)
    
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)