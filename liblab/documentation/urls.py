from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_sidebar_data, name='sidebar'),
    path('document/<slug:slug>/', views.document_detail, name='document_detail'),
]
