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