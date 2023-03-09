from django.db import models

# Create your models here.
class landing(models.Model):
	TYPE_BLOCK = [
        ('themes', 'Типизированный'),
        ('null', 'Пустой'),
        ('html', 'Произвольный'),
        ('js', 'JS'),
        ('scc', 'Cтили'),
    ]


	title = models.CharField(max_length=255,verbose_name="Заголовок")
	name = models.CharField(max_length=255,blank=True,null=True,verbose_name="Название")
	content = models.TextField(blank=True,verbose_name="Настройки")
	photo = models.URLField(max_length=255,blank=True,verbose_name="Изображения")	
	time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
	time_update = models.DateTimeField(auto_now=True,verbose_name="Последнее обновление")
	order = models.IntegerField(blank=True,null=True,verbose_name="Порядок")
	type_block = models.CharField(max_length=255,verbose_name="Тип",blank=True,null=True,choices=TYPE_BLOCK)
	is_published = models.BooleanField(default=True,verbose_name="Видимость")
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('post', kwargs={'post_id': self.pk})

	class Meta:
		verbose_name = 'Блок'
		verbose_name_plural = 'Блоки'

class Files(models.Model):
	TYPE_FILE_UP = [
        ('image', 'Изображения'),
        ('doc', 'Документ'),
        ('vido', 'Видео'),
        ('audio', 'Аудио'),
        
    ]


	title = models. CharField (max_length=255,blank=True,verbose_name="Заголовок")
	type_file = models.TextField(blank=True,verbose_name="Тип файла",choices=TYPE_FILE_UP)
	data = models.FileField(upload_to="files/%Y/%m/%d/",blank=False,verbose_name="Фаил")	
	time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время загрузки")
	time_update = models.DateTimeField(auto_now=True,verbose_name="Последнее обновление")
	is_published = models.BooleanField(default=True,verbose_name="Опубликованно")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('post', kwargs={'post_id': self.pk})

	class Meta:
		verbose_name = 'Фаил'
		verbose_name_plural = 'Файлы'

class bids(models.Model):
	STATUS_BID = [
        ('new', 'Новая'),
        ('processing', 'Обработка'),
        ('completed', 'Завершенна'),        
    ]

	name = models.CharField(max_length=100, db_index=True,verbose_name="Имя",blank=True)
	last_name = models.CharField(max_length=100, db_index=True,verbose_name="Фамилия",blank=True)
	mail = models.CharField(max_length=100, db_index=True,verbose_name="Почта",blank=True)
	tel = models.CharField(max_length=100, db_index=True,verbose_name="Телефон",blank=True)
	message = models.TextField(db_index=True,verbose_name="Сообщение",null=True,blank=True)	
	which = models.CharField(max_length=100, db_index=True,verbose_name="Форма отправки",blank=True)
	ip = models.CharField(max_length=100, db_index=True,verbose_name="IP",blank=True)
	country = models.CharField(max_length=100, db_index=True,verbose_name="Страна",blank=True)
	os = models.CharField(max_length=100, db_index=True,verbose_name="Операционная система",blank=True)
	browser = models.CharField(max_length=200, db_index=True,verbose_name="Браузер",blank=True)
	data = models.FileField(upload_to="files/%Y/%m/%d/",blank=True,verbose_name="Фаил")
	time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время отправки",blank=True)
	time_update = models.DateTimeField(auto_now=True,verbose_name="Последнее обновление",blank=True)
	status = models.TextField(blank=True,verbose_name="Статус",choices=STATUS_BID)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse ('post', kwargs={'post_id': self.pk})

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'

class visitors(models.Model):
	ip = models.CharField(max_length=100, db_index=True,verbose_name="IP",blank=True)
	browser = models.CharField(max_length=200, db_index=True,verbose_name="Браузер",blank=True)
	time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время посещения",blank=True)
	time_out = models.CharField(max_length=100, db_index=True,verbose_name="Время ухода",blank=True)

	def __str__(self):
		return self.ip

	class Meta:
		verbose_name = 'Посетитель'
		verbose_name_plural = 'Посетители'

class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	# time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
	# time_update = models. DateTimeField (auto_now=True,verbose_name="Последнее обновление")
	
	def __str__(self):
		return self.name

class Brick(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	friends = models.ManyToManyField('Brick',blank=True, null=True)
	# time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
	# time_update = models. DateTimeField (auto_now=True,verbose_name="Последнее обновление")
	
	def __str__(self):
		return self.name

