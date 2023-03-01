from django.http import HttpResponse,HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

import json


class LandingHome(ListView):
	model = landing
	template_name = 'landing/index.html'
	context_object_name ='all'
	#extra_context = {'title':'ООО Сисадмин — Обслуживание информационых систем'}

	def get_context_data(self,*, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)

		blocks = landing.objects.filter(is_published=True).order_by('order')
		new_dictData = {}

		context['title'] = 'ООО Сисадмин — Обслуживание информационых систем'

		for i in range(len(blocks)):
			#print(blocks[i].title)

			settings_block = blocks.filter(title=blocks[i].title)[0].content
			if settings_block != '':
				context[blocks[i].title] = json.loads(settings_block)
			else:
				context[blocks[i].title] = ''
		
		return context

	def get_queryset(self):
		return landing.objects.filter(is_published=True).order_by('order')

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

	return render(request,'landing/index.html',new_dictData)

class SortingHome(LoginRequiredMixin,ListView):
	model = landing
	template_name = 'accounts/sorting.html'
	context_object_name ='items'
	ordering = ['order']
	login_url = '/admin/'
	#raise_exception = True

class DashboardPage(LoginRequiredMixin,ListView):
	model = landing
	template_name = 'accounts/darkpan/index.html'
	context_object_name ='items'
	ordering = ['order']
	login_url = '/admin/'
	
	

# def sorting(request):

# 	blocks = landing.objects.all()
# 	new_dictData = {}

# 	for i in range(len(blocks)):
# 		#print(blocks[i].title)

# 		settings_block = blocks.filter(title=blocks[i].title)[0].content
# 		new_dictData['items'][blocks[i].title] =settings_block

# 	return render(request,'landing/sorting.html',new_dictData)


def postOut(request):
	errors = ''
	print(request.POST)
		

	try:
		name = request.POST['name']
		#tel = request.POST['telephone']
		#message = request.POST['message']
		from_name = request.POST['form_name']
		browser = request.META.get('HTTP_USER_AGENT')
		ip = request.META.get('REMOTE_ADDR')		
	except:
	 	return HttpResponse('Ошибка формы')


	arr_filds = ['email','telephone','message','last_name']
	for i in range(len(arr_filds)):
		if arr_filds[i] not in request.POST:
			globals()[arr_filds[i]] = ''
		else:
			globals()[arr_filds[i]] = request.POST[arr_filds[i]]


	if request.POST['name'] == '' :
		errors = 'name/'

	if request.POST['telephone'] == '' :
		errors += 'telephone/'
	
	if errors != '' :
		return HttpResponse(errors)

	p = bids(
		name=name,
		last_name=last_name,
		mail=email,
		tel=telephone,
		message=message,
		which=from_name,
		browser=browser,
		ip=ip,
		status='new'
		)
	p.save()

	# print(locals())
	# print(telephone)
	return HttpResponse('Cообщение отправленно')

@login_required
def sort_blocks(request):
	
	sorted_ids = request.POST.getlist('sort_order')

	arr_tmp = sorted_ids[0].split('&')

	arr_out = []

	for i in range(len(arr_tmp)):
		arr_out.append(arr_tmp[i].split('[]=')[1])

	#blocks = landing.objects.all()

	for i in range(len(arr_out)):
		print(arr_out[i])
		#blocks.filter(title=arr_out[i])[0].order = i

		instance = landing.objects.filter(pk=arr_out[i])[0]
		print(instance.order)
		print(i)
		instance.order = i
		instance.save()

	

	print(arr_out)

	return HttpResponse('не получен список сортировки ')


def pageNotFound(request,exception):
	#return HttpResponseNotFound('Страница не найдена')
	return render(request,'landing/404.html')






