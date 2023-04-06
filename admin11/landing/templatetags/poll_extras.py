# Добовление пользовательских фильтров шаблона
from django import template
from landing.models import *
#from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

import json

# Обязательная регистрация 
register = template.Library()

# Для тегов
# siple_tag()

@register.filter(name='test')
def cut(value, arg):	
	return 'work'

@register.filter()
def get_form(value):

	print(type(value))
	fields = ''
	

	if 'name' in value:
		fields +='''
			<div class="form-floating mb-3">
				<input name="name" type="text" class="form-control" id="floatingInput" placeholder="123">
				<label for="floatingInput">Имя</label>
			</div>'''

	if 'email' in value:
		fields +='''
			<div class="form-floating mb-3">
				<input name="telephone" type="tel" class="form-control" id="floatingTel" placeholder="+" maxlength="18" data-tel-input>
				<label for="floatingTel">Телефон</label>
			</div>'''

	if 'message' in value:   
		fields +='''
			<div class="form-floating mb-3">
				<textarea name="message" class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
				<label for="floatingTextarea2">Сообщение</label>
			</div>''' 



	return mark_safe(fields)



@register.filter(name='myjoin')
def cut(value):	
	return 'landing/'+value+'.html'

@register.simple_tag(name='myinclude')
def my_include(value):
	#print(value)
	return 'landing/'+value+'.html'

@register.filter(name='strtoarr')
def my_include(value):
	#print(value)
	return json.loads(value, strict=False)


@register.filter(name='my_type')
def my_type(value):
    return type(value).__name__