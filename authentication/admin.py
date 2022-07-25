from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    field_sets = (
        ('Bio-Data', {
            'fields': ('username',
                        ('first_name', 'last_name'),
                        ('email', 'location'),
                        'date_of_birth', 'profile_picture')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)
