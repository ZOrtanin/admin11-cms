from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

from .models import *


from django.forms.widgets import Widget
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

import json


def modulinput(string,value):

	out_form = '<div class="mb-3">'

	if string != '':
		out_form += f'<label class="col-form-label"  for="id_name">{string}:</label>'

	print(len(value))

	if len(value) > 50 :
		out_form +=f'<textarea class="form-control">{value}</textarea>'
	else:
		out_form +=f'<input class="form-control" type="text" value="{value}">'

	out_form += '</div>'

	return out_form


class MyWidget(forms.widgets.Widget):
	template_name = 'my_widget.html'

	def __init__(self, attrs=None):
		super().__init__(attrs)

	def render(self, name, value, attrs=None, renderer=None):
		context = self.get_context(name, value, attrs)
		
		out_form = ''

		arr_filds = json.loads(value)
		print(len(arr_filds))

		for item in arr_filds:	
			out_form += '<h3>'+str(item)+'</h3>'

			if not isinstance(arr_filds[item], str):	

				for inp in arr_filds[item]:
					print(str(inp) + ' - '+str(type(inp)))

					if isinstance(inp, str):
						out_form += modulinput(inp,arr_filds[item][inp])
						# out_form += f'''
						# 		<div class="mb-3">
						# 		<label class="col-form-label" for="id_name">{inp}:</label>
						# 		<input class="form-control" type="text" name="name" value="{arr_filds[item][inp]}">
						# 		</div>
						# 		'''
					else:
						# out_form += '<p>'
						# out_form += inp['label']

						for string in inp:
							# out_form += string
							out_form += modulinput(string,inp[string])
							# out_form += f'''
							# 	<div class="mb-3">
							# 	<label class="col-form-label" for="id_name">{string}:</label>
							# 	<input class="form-control" type="text" name="name" value="{inp[string]}">
							# 	</div>
							# 	'''

						# out_form += '</p>'

			else:
				out_form += modulinput('',arr_filds[item])
				# out_form += f'''
				# 		<div class="mb-3">    				
	    		# 		<input class="form-control" type="text" name="name" value="{arr_filds[item]}">
	  			# 		</div>
				# 		'''


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

	#content = forms.CharField(widget=forms.Textarea(attrs={ 'cols':30,'rows': 10}))
	content = forms.CharField(widget=MyWidget)
	
	class Meta:
		model = landing
		fields = ['name','content','is_published']

		# print('123')
		# print(content)










