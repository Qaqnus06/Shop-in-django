from django.contrib import admin
from .models import Place,Owner,PlaceOwner,Comment




class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','last_name')
    search_fields = ('first_name',)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name','adress')
    search_fields = ('name',)
    list_per_page = 100
    list_display_links=('name',)

class PlaceOwnerAdmin(admin.ModelAdmin):
    list_display = ('id','place','owner')
    search_fields = ('place','owner')
    list_filter=('place',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','place','comment_text','stars_given')
    search_fields = ('place','user') 
    save_as = False
    list_filter=('place',)
      
admin.site.register(Place,PlaceAdmin)
admin.site.register(Owner,OwnerAdmin)
admin.site.register(PlaceOwner,PlaceOwnerAdmin)
admin.site.register(Comment,CommentAdmin)