from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
#from landing.models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ['first_name', 'last_name']
#     ordering = ['first_name']

#     def get_user_model(self, request):
#     	return CustomUser

# admin.site.register(CustomUser, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)


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

class VisitorsAdmin(admin.ModelAdmin):
	list_display = ('ip', 'browser', 'time_create','time_out')

admin.site.register(visitors,VisitorsAdmin)

admin.site.register(Files)

#admin.site.register(Category)
#admin.site.register(Brick)
