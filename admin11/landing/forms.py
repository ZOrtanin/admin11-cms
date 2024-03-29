from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

from .models import *


from django.forms.widgets import Widget
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

import json



def modulinput(string,value,block,label=True):
	out_form = ''
	if str(type(value)) == "<class 'dict'>":
		#print("work1")
		#print(string)
		#print(type(value))

		out_form +=	f'<div class="col {string}-admin" name="{string}">'
		out_form += '<h3>'+str(string)+'</h3>'
		for inp in value:
			out_form += modulinput(inp,value[inp],block)
		out_form += '</div>'

	else:

		if string != block :

			out_form = f'<div name="{string}" class="mb-3 px-4 row">'

			# if string != '':
			# 	print(label)
			# 	out_form += f'<label class="col-form-label"  for="id_name">{string}:</label>'

			if label != False:
				print(label)
				out_form += f'<label class="col-form-label" for="id_name">{string}:</label>'

			#print(len(value))

			if string == 'image':
				out_form +=f'<div class="col-2 btn btn-warning me-1 px-1 add-file-base overflow-hiden" data-bs-toggle="modal" data-bs-dismiss="modal" data-bs-target="#ModalFiles"><i class="fa-regular fa-image"></i></div>'

			if len(value) > 50 and string != 'image' :
				out_form +=f'<textarea class=" form-control" type="text" name="{string}-{block}" rows="10">{value}</textarea>'
			
			else:
				out_form +=f'<input class="col form-control" type="text" name="{string}-{block}" value="{value}" aria-describedby="button-addon1">'

			

			out_form += '</div>'
		else:
			out_form=''

	return out_form


class MyWidget(forms.widgets.Widget):
	template_name = 'my_widget.html'

	def __init__(self, type_block=None, attrs=None):
		self.type_block = type_block
		super().__init__(attrs)

	def render(self, name, value, attrs=None, renderer=None):
		context = self.get_context(name, value, attrs)
		out_form = '<div class="content_admin row">'
		

		if self.type_block != 'themes':
			out_form += f'<textarea name="content" class="form-control" rows="20">{value}</textarea>'
		else:
			print(str(value))
			arr_filds = json.loads(value, strict=False)
			print(arr_filds)

			for item in arr_filds:
				

				#print('work')
				if 'item' in arr_filds[item]:
					#print('есть')
					add_block = ''
					col = 'col'
					
					try:
						if arr_filds[item]['add_block'] == 'true':
							add_block = 'add_block'
							col = 'col-3'
					except:
						pass

					out_form +=	f'<div class="col-12 {item}-admin {add_block} row" name="{item}">'
					out_form += '<h3>'+str(item)+'</h3>'
					
					for child in arr_filds[item]['item']:
						#print(child)
						out_form += f'<div class="item {col} ms-1" name="item" style="background-color:rgb(218, 230, 237);padding:5px ; border-radius: 9px; margin-bottom: 10px;">'
						for inp in child:
							#print(inp)
							out_form += modulinput(inp,child[inp],item)
						out_form += '</div>'
					
				else:
					#print('нету')
					out_form +=	f'<div class="col-12 {item}-admin row" name="{item}">'
					out_form += '<h3>'+str(item)+'</h3>'

					#print(arr_filds[item])
					for inp in arr_filds[item]:
						#print(arr_filds[item][inp])
						out_form += modulinput(inp,arr_filds[item][inp],item)
				#print(type(arr_filds[item]))

				out_form += '</div>'


		out_form +='</div>'


		context['form'] = out_form		
		return render_to_string(self.template_name, context)

	def render_old(self, name, value, attrs=None, renderer=None):
		context = self.get_context(name, value, attrs)
		
		out_form = '<div class="content_admin row">'

		#print(self.get_context(name, value, attrs))
		
		#print(str(self.type_block)+' --++')

		if self.type_block != 'themes':
			out_form = f'<textarea name="content" class="form-control" rows="20">{value}</textarea>'
		else:
			arr_filds = json.loads(value)
			#print(len(arr_filds))		

			for item in arr_filds:
				out_form +=	f'<div class="col-4 {item}" name="{item}">'
				out_form += '<h3>'+str(item)+'</h3>'

				if not isinstance(arr_filds[item], str):				

					for inp in arr_filds[item]:
						#print(str(inp) + ' - '+str(type(inp)))
						#print('work2')

						if isinstance(inp, str):
							#print('work1 '+ str(type(inp)) + ' - ' + str(type(arr_filds[item])))

							out_form += modulinput(inp,arr_filds[item][inp],item)

						else:						
							out_form += '<div name="item" style="background-color:rgb(218, 230, 237);padding:5px ; border-radius: 9px; margin-bottom: 10px;">'
							for string in inp:								
								out_form += modulinput(string,inp[string],item)
							out_form += '</div>'			

				else:
					out_form += modulinput(item,arr_filds[item],item,label=False)
					
			
				out_form += '</div>'	

		out_form += '</div>'
		context['form'] = out_form

		
		return render_to_string(self.template_name, context)


class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'123'}))
	email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'123'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'123'}))
	password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'123'}))

	class Meta:
		model = User
		fields = ('username','email','password1','password2')


class EditContentFormTutor(forms.Form):
	
	title = forms.CharField(max_length=255)
	slug = forms.SlugField (max_length=255)
	content = forms. CharField(widget=forms.Textarea(attrs={ 'rows': 10}))
	is_published = forms. BooleanField()
	cat = forms. ModelChoiceField(queryset=Category.objects.all ())


class EditContentForm(forms.ModelForm):
	
	#type_block = '123'
	
	
	class Meta:
		model = landing
		fields = ['name','type_block','content','is_published']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#print(str(self.initial.get('type_block'))+' ---')

		type_block = self.initial.get('type_block')
		#content = forms.CharField(widget=MyWidget(type_block))

		self.fields['content'].widget = MyWidget(type_block=type_block)

	def get_type():
		return self.initial.get('type_block')

	#content = forms.CharField(widget=forms.Textarea(attrs={ 'cols':30,'rows': 10}))
	#type_block = forms.CharField(widget=forms.Textarea(attrs={ 'cols':30,'rows': 10}))
	# print('123')
	# print(content)










