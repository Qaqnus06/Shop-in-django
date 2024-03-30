from django.contrib import admin
from.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_display_links=('username',)
    search_fields=('username',)


admin.site.register(User,UserAdmin)
