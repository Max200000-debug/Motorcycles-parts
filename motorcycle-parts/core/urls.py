from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/view/', views.SingleView.as_view(), name='single'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('add/', views.AddView.as_view(), name='add'),
    path('<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    path('<int:id>/save/', views.save, name='save'),
    path('shipments/create/', views.CreateShipment.as_view(), name='create-shipment'),
    path('shipments/process/', views.process_shipment, name='process-shipment'),
    path('shipments/<int:pk>/', views.ViewShipmentSingle.as_view(), name='single-shipment'),
    path('shipments/', views.ViewShipments.as_view(), name='shipments'),
]