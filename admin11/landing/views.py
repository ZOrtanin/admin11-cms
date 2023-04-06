from django.http import HttpResponse,HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout

from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .utils import *
from .forms import *
#from .urls import *

import json
from datetime import datetime
from bs4 import BeautifulSoup


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

            settings_block = blocks.filter(title=blocks[i].title)[0]
            if settings_block.content != '':
                if settings_block.type_block != 'html':
                    context[blocks[i].title] = json.loads(settings_block.content)
                else:
                    context[blocks[i].title] = settings_block.content
            else:
                context[blocks[i].title] = ''
        
        # print(self.request.user.is_authenticated)
        num_visits=self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits+1
        print(str(num_visits)+' <---')

        if not self.request.user.is_authenticated:
            visitor = visitors(
            ip=self.request.META.get('REMOTE_ADDR'),
            browser=self.request.META.get('HTTP_USER_AGENT'),    
            time_out=self.request.session.get('num_visits', 0)    
            )
            visitor.save()

        return context

    def get_queryset(self):
        return landing.objects.filter(is_published=True).order_by('order')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/darkpan/signup.html'
    success_url = reverse_lazy('landing:login')
    
    def get_context_data(self, *, object_list=None, **kwargs) :
        context = super () .get_context_data(**kwargs)
        c_def = self.get_user_context (title="Регистрация")

        return dict(list(context.items ()) + list(c_def.items ()))

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/darkpan/signin.html'

    def get_context_data(self, *, object_list=None, **kwargs) :
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")

        return dict(list (context.items ()) + list(c_def.items ()))

    def get_success_url(self):
        return reverse_lazy('landing:dashboard')
        #return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('landing:login')

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

    #print(new_dictData['hero'])    

    return render(request,'landing/index.html',new_dictData)

class SortingHome(LoginRequiredMixin,ListView):
    model = landing
    template_name = 'accounts/sorting.html'
    context_object_name ='items'
    ordering = ['order']
    login_url = '/admin/'
    #raise_exception = True

class DashboardPage(LoginRequiredMixin,DataMixin,ListView):
    model = landing
    template_name = 'accounts/darkpan/dashboard.html'
    context_object_name ='items'
    ordering = ['order']
    login_url = '/admin/'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['user'] = self.request.user
        context['orders'] = bids.objects.order_by("-id")[0:5]
        context['orders_count'] =bids.objects.count()
        context['visitors_count'] = visitors.objects.filter(time_out='1').count()
        context['reload_page_count'] = visitors.objects.count()
        context['ip_count'] = visitors.objects.values('ip').distinct().count()
        c_def = self.get_user_context(title="Панель упровления",selected="landing:dashboard")
        context = dict(list(context.items())+list(c_def.items()))
        return context

    
class EditMode(LoginRequiredMixin,DataMixin,ListView):
    model = landing
    template_name = 'accounts/darkpan/edit_mode.html'
    context_object_name ='all'    
    login_url = '/admin/'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        blocks = landing.objects.all().order_by('order')
        new_dictData = {}

        context['title'] = 'ООО Сисадмин — Обслуживание информационых систем'
        context['edit_mode']='True'
       

        for i in range(len(blocks)):
            #print(blocks[i].title)

            settings_block = blocks.filter(title=blocks[i].title)[0]
            if settings_block.content != '':
                if settings_block.type_block != 'html':
                    #print(blocks[i].title)
                    new_blocks = ['header','hero','introductory','price']

                    if str(blocks[i].title) in new_blocks:
                        context[blocks[i].title] = json.loads(settings_block.content, strict=False)
                        context[blocks[i].id] = json.loads(settings_block.content, strict=False)
                    else:
                        context[blocks[i].title] = json.loads(settings_block.content, strict=False)
                        context[blocks[i].id] = json.loads(settings_block.content, strict=False)

                    
                    #print(context[blocks[i].title])
                else:
                    context[blocks[i].title] = settings_block.content
            else:
                context[blocks[i].title] = ''
        
        return context

    def get_queryset(self):
        return landing.objects.all().order_by('order')

@login_required
def EditModeDisableBlock(request,id_block):

    block = landing.objects.get(id = id_block)
    #print(block.)

    if block.is_published == False:
        block.is_published = True
    else:    
        block.is_published = False

    block.save()

    #return redirect('/edit/#'+block.title)
    return HttpResponse('Good')

@login_required
def EditModeSaveBlock(request,id_block):
    block = landing.objects.get(id=id_block)
    
    if request.POST.getlist('content'):
        block.content = request.POST.getlist('content')[0]
        block.save()
    else:
        print('Ключа нет')
        #print(request.POST)
        html = str(request.POST.getlist('content_admin'))
        # print('')
        # print(html)
        # print('')
        soup = BeautifulSoup('<div name="main">'+html+'</div>','html.parser')
        json_obj = parse_element(soup.find('div'),0,'main')
        
        out2 = str(json_obj).replace('"', "'")
        #out2 = out2.replace('"', "'")

        print(out2.replace('\\', "  ").replace("'", '"').replace('  "', "'"))

        block.content = out2.replace('\\', "  ").replace("'", '"').replace('  "', "'")
        block.save()

        #print(request.POST.getlist('content_admin'))

        # html = str(request.POST.getlist('content_admin'))       
        # soup = BeautifulSoup('<div>'+html+'</div>','html.parser')        

        # json_obj = parse_element_new(soup.find('div'))
        # print(json_obj)

        

    print(request.POST.getlist('content'))
    return redirect('landing:edit')

@login_required
def sort_blocks(request):    

    # print(arr_out)
    sorted_ids = request.POST.getlist('dataset')
    json_sorted = json.loads(sorted_ids[0])

    arr_out = []

    for i in range(len(json_sorted)):
        arr_out.append(json_sorted[str(i)]['id_element'])

    # #blocks = landing.objects.all()

    for i in range(len(arr_out)):
        print(arr_out[i])
        #blocks.filter(title=arr_out[i])[0].order = i

        instance = landing.objects.filter(pk=arr_out[i])[0]
        print(instance.order)
        print(i)
        instance.order = i
        instance.save()

    return HttpResponse('Список сортировки обновлен')

def EditBlockFunc(request):
    return HttpResponse('работает')

class EditBlock(LoginRequiredMixin,DataMixin,ListView):
    model = landing
    template_name = 'modals/header.html'
    context_object_name ='all'    
    object_list = landing.objects.all()


    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование блока'

        # нужно передать id
        print(self.kwargs['id_block'])
        landing_obj = get_object_or_404(landing, id=int(self.kwargs['id_block']))        
        form = EditContentForm(instance=landing_obj)
        #form = EditContentForm()
        context['form'] = form        
        return context

    def post(self, request, *args, **kwargs):        
        # Отобразить шаблон и передать контекст данных
        return render(request, self.template_name, self.get_context_data())

    

    # context_object_name ='all'
    # form_class = EditContentForm
    # login_url = '/admin/'

    # def get_context_data(self,*, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     return context

    # def get_queryset(self):
    #     return landing.objects.all()


class OrderPage(LoginRequiredMixin,DataMixin,ListView):
    model = landing
    template_name = 'accounts/darkpan/order.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['user'] = self.request.user
        context['orders'] = bids.objects.order_by("-id")
        context['orders_count'] =bids.objects.count()
        c_def = self.get_user_context(title="Заявки",selected="landing:order")
        context = dict(list(context.items())+list(c_def.items()))
        return context

@login_required
def getOrderOut(request, order_id):
    order = bids.objects.get(id=order_id)    
    out_line = {}
    out_line['order'] = order

    print(order.STATUS_BID[0][0])

    return render(request,'modals/order.html',out_line)

@login_required
def OrderEdit(request, order_id):
    print(request.POST)
    print(order_id)
    order = bids.objects.get(id=order_id)


    if order.status != request.POST['status']:
        order.status = request.POST['status']
        order.message = order.message 
        order.message +='\n-------\n'

        for item in order.STATUS_BID:
            if item[0] in request.POST['status']:
                order.message +='Изменен статус на \n'+ item[1] +'\n'

        order.message += str(datetime.now())

    if request.POST['text-attach'] != '':
        order.message = order.message 
        order.message +='\n-------\n'
        order.message +='Заметка:\n'
        order.message += request.POST['text-attach']+'\n'
        order.message += str(datetime.now())

    order.save()

    if request.POST['page']=='dashboard':
        return redirect('landing:dashboard')

    return redirect('landing:order')

@login_required
def OrderDel(request, order_id):
    record = bids.objects.get(id = order_id)
    record.delete()

    return redirect('landing:order')

class UsersPage(LoginRequiredMixin,DataMixin,ListView):
    model = landing
    template_name = 'accounts/darkpan/users.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['user'] = self.request.user
        context['visitors'] = visitors.objects.order_by("-id")
        context['visitors_count'] = visitors.objects.count()
        c_def = self.get_user_context(title="Посетители",selected="landing:users")
        context = dict(list(context.items())+list(c_def.items()))
        return context

class FilesPage(LoginRequiredMixin,DataMixin,ListView):
    model = landing
    template_name = 'accounts/darkpan/files.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['user'] = self.request.user
        context['orders'] = bids.objects.order_by("-id")
        context['orders_count'] =bids.objects.count()
        c_def = self.get_user_context(title="Файлы",selected="landing:files")
        context = dict(list(context.items())+list(c_def.items()))
        return context

# def sorting(request):

#     blocks = landing.objects.all()
#     new_dictData = {}

#     for i in range(len(blocks)):
#         #print(blocks[i].title)

#         settings_block = blocks.filter(title=blocks[i].title)[0].content
#         new_dictData['items'][blocks[i].title] =settings_block

#     return render(request,'landing/sorting.html',new_dictData)

@login_required
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


def pageNotFound(request,exception):
    #return HttpResponseNotFound('Страница не найдена')
    return render(request,'landing/404.html')

def parse_element(element,level,level_name,item=[]):
    obj = {}
    name = level_name
    flag = False
    num=0  

    # Добавляем атрибуты элемента в объект
    for attr, value in element.attrs.items():        
        if attr == 'name':            
            name = value

        if attr == 'name' and value == 'item':
            #print('+')
            flag = True

    mychild={}
    for child in element.children:

        if child.name:
            if level_name == name:                
                
                new_element = parse_element(child,1,name,item=[])
            else:
                new_element = parse_element(child,1,name,item)
            

            if new_element != {}:
                neme_first = list(new_element.keys())[0]

                if 'type' in new_element and flag == False:
                    #print(child.name)
                    if child.name != 'textarea':
                        obj[name] = new_element['value']
                    else:
                        obj[name] = child.text

                elif flag == True:
                    mychild[neme_first]= new_element[neme_first]                    

                else:
                    if level_name != name:
                        obj[neme_first] = new_element[neme_first]
                    else:
                        obj[neme_first] = new_element
            else:
                obj[name] = name
                
    if flag == True :

        item.append(mychild)
        obj['item']=item
        num+=1
        

    # Добавляем атрибуты элемента в объект
    for attr, value in element.attrs.items():        
        if 'type' in element.attrs:            
            obj[attr]=value

    return obj
