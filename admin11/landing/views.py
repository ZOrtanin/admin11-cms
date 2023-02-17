from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

from .models import *

import json

# Create your views here.
def title(request):
	# key = request.GLOBAL
	# print(key)
	#return HttpResponse('Привет мир ')

	settings_header = landing.objects.filter(title='header')

	blocks = landing.objects.all()

	header = json.loads(blocks.filter(title='header')[0].content)

	#print(blocks[0].title)

	new_dictData = {}

	for i in range(len(blocks)):
		#print(blocks[i].title)

		settings_block = blocks.filter(title=blocks[i].title)[0].content
		new_dictData[blocks[i].title] = json.loads(settings_block)

	print(new_dictData['hero'])

	#string = '{"logo":{"image":"/images/logo.svg","link":"/"},"menu":[{"label":"Цены","link":"#price"},{"label":"Особенности","link":"#features"},{"label":"О Нас","link":"#about"},{"label":"Контакты","link":"#contacts"}],"social-link":[{"label":"whatsapp","link":""},{"label":"telegram","link":""}]}'
	#print(settings_header[0].content)

	#dictData = json.loads(settings_header[0].content)
	# dictionary = {
	# # 'menu':dictData['menu'],
	# # 'logo':dictData['logo'],
	# # 'social_link':dictData['social-link'],
	# 'blocks':blocks,
	# 'header':{
	# 		'menu':dictData['menu'],
	# 		'logo':dictData['logo'],
	# 		#'social_link':dictData['social-link'],
	# 	}
	# }

	return render(request,'landing/index.html',new_dictData)

def postOut(request):
	errors = ''
	print(request.POST)
		

	try:
		name = request.POST['name']
		tel = request.POST['telephone']
		message = request.POST['message']
	except:
		return HttpResponse('Ошибка формы')


	if request.POST['name'] == '' :
		errors = '<p>Напишите свое имя</p>'

	if request.POST['telephone'] == '' :
		errors += '<p>Напишите свой телефон</p>'
	
	if errors != '' :
		return HttpResponse(errors)

	print(request.POST)
	return HttpResponse('Cообщение отправленно '+str(tel)+' '+name)

def pageNotFound(request,exception):
	#return HttpResponseNotFound('Страница не найдена')
	return render(request,'landing/404.html')
