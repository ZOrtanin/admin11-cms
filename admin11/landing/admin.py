from django.contrib import admin
from .models import *

class LandingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')
	list_editable = ('is_published' ,)
	list_filter = ('is_published', 'time_create')

admin.site.register(landing,LandingAdmin)

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
