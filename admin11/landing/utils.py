from .models import *


class DataMixin:
	def get_user_context(self, **kwargs):
		context = kwargs
		context['menu_admin']=[{'title':'Панель','url_name':'landing:dashboard','icon':'fa-tachometer-alt'},
							   {'title':'Режим ред.','url_name':'landing:edit','icon':'fa-edit'},
							   {'title':'Заявки','url_name':'landing:order','icon':'fa-shopping-basket'},
							   {'title':'Посетители','url_name':'landing:users','icon':'fa-users'},
							   {'title':'Файлы','url_name':'landing:files','icon':'fa-folder-open'},
							   {'title':'Настройки','url_name':'landing:settings','icon':'fa-gear'},
							   
			]

		return context