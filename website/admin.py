from django.contrib import admin
from .models import Enquiry, GalleryProject 


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'message',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    ordering = (
        '-created_at',
    )

    list_editable = (
        'status',
    )

    fieldsets = (
        (
            'Customer Information',
            {
                'fields': (
                    'name',
                    'email',
                    'phone',
                )
            }
        ),
        (
            'Enquiry Details',
            {
                'fields': (
                    'message',
                    'status',
                )
            }
        ),
        (
            'System Information',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )

@admin.register(GalleryProject)
class GalleryProjectAdmin(admin.ModelAdmin):

     list_display = (
        'title',
        'category',
        'location',
        'is_featured',
        'created_at',
    )

     list_filter = (
        'category',
        'is_featured',
        'created_at',
    )

     search_fields = (
        'title',
        'location',
        'description',
    )

     list_editable = (
        'is_featured',
    )

     ordering = (
        '-created_at',
    )