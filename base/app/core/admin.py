from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _

@admin.register(models.User)
class Profile(BaseUserAdmin):

    ordering = ['id']
    list_display = ['email', 'name', 'phone_number', 'website', 'picture']
    list_display_links = ('email', 'phone_number')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name','last_name','phone_number')}),
        (_('location'), {'fields': ('city','country')}),
        (_('social'), {'fields': ('website','biography','picture')}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important date'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

