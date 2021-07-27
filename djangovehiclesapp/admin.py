""" docstring """


from django.contrib import admin
from .models import Vehicle, VehicleManufacturer, VehicleModel, VehicleVersion


@admin.register(VehicleManufacturer)
class VehicleManufacturerAdmin(admin.ModelAdmin):
    """  """

    list_display = [
        "id",
        "name",
    ]

    list_display_links = [
        "id",
        "name",
    ]
    
    search_fields = [
        "id",
        "name",
    ]


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "manufacturer",
        "name",
        "year",
    ]

    list_display_links = [
        "id",
        "manufacturer",
        "name",
        "year",
    ]

    list_filter = [
        "manufacturer",
        "year",
    ]
    
    search_fields = [
        "manufacturer",
        "name",
    ]

    list_select_related = [
        "manufacturer",
    ]

    autocomplete_fields = [
        "manufacturer",
    ]


@admin.register(VehicleVersion)
class VehicleVersionAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "model",
    ]

    list_display_links = [
        "name",
        "model",
    ]
    
    list_filter = [
        "name",
        "model",
    ]

    search_fields = [
        "name",
        "model",
    ]

    list_select_related = [
        "model",
    ]

    autocomplete_fields = [
        "model",
    ]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = [
        "manufacturer",
        "model",
        "version",
    ]

    list_display_links = [
        "manufacturer",
        "model",
        "version",
    ]
    
    list_filter = [
        "manufacturer",
        "model",
    ]

    search_fields = [
        "manufacturer",
        "model",
        "version",
    ]

    list_select_related = [
        "manufacturer",
        "model",
        "version",
    ]

    autocomplete_fields = [
        "manufacturer",
        "model",
        "version",
    ]
