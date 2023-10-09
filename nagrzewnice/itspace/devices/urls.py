from django.urls import path
from  devices.views import DevicesListView, DeviceDetailsView



urlpatterns = [
    path('device/<int:device_id>/', DeviceDetailsView.as_view(), name='device_details'),
    path('', DevicesListView.as_view(), name='devices_list'),
]
