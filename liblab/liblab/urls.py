# documentation_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Add include here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('documentation.urls')),  # Include documentation app URLs
]
