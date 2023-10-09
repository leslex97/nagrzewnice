from django.contrib import admin

from devices.models import Device, Switches, DeviceType


class DeviceAdmin(admin.ModelAdmin):
    
    list_display = ["name", 'type', "iP", 'place', 'switch' ]
    
    search_fields=["name" , "iP","switch__switch_name", "type__name"]
    
    list_filter=[
        "switch__switch_name",
        "type__name"
        ]

class SwithesAdmin(admin.ModelAdmin):
    
    list_display = ["switch_name",
                    "switch_place",
                    "switch_ip",
                    "switch_model", ]
    
    search_fields = ["switch_name", "switch_ip"]
    
    list_filter=["switch_model"]

admin.site.register(Device, DeviceAdmin)
admin.site.register(Switches, SwithesAdmin)
admin.site.register(DeviceType)
