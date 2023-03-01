from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin
from .models import *

class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ('id', 'title','name','time_update','is_published','type_block','order')
	list_display_links = ('id', 'title')
	list_editable = ('is_published' ,'type_block')
	search_fields = ('title', 'content')
	list_filter = ('is_published', 'time_update')
	ordering=('order',)

class LandingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'time_update','is_published','type_block','order')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')
	list_editable = ('is_published' ,'order','type_block')
	list_filter = ('is_published', 'time_update')
	ordering=('order',)

	

	# @admin.display(ordering='order')

admin.site.register(landing,MyModelAdmin)

class BidsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','message','which','time_create','status')
	list_display_links = ('id', 'name')
	# search_fields = ('title', 'content')
	# list_editable = ('is_published' ,)
	list_filter = ('time_create','status','which')
admin.site.register(bids,BidsAdmin)
#admin.site.register(bids)

admin.site.register(Files)

#admin.site.register(Category)
#admin.site.register(Brick)
