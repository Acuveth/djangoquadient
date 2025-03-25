from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/portal/', permanent=True)),
    path('portal/', include('api_client.urls')),

    # Add authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]