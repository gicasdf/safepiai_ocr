from django.urls import path
from ocrapi import views

urlpatterns = [
    path('ocrapi/', views.snippet_list),
    path('ocrapi/<int:pk>', views.snippet_detail),
]
