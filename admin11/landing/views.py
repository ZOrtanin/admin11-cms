from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def title(request):
	# key = request.GLOBAL
	# print(key)
	#return HttpResponse('Привет мир ')
	return render(request,'landing/index.html')

def pageNotFound(request,exception):
	return HttpResponseNotFound('Страница не найдена')
