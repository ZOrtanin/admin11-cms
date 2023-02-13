from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def title(request):
	# key = request.GLOBAL
	# print(key)
	#return HttpResponse('Привет мир ')
	return render(request,'landing/index.html')

def postOut(request):
	errors = ''

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
