from django.db import models

# Create your models here.
class landing(models.Model):
	YEAR_IN_SCHOOL_CHOICES = [
        ('FRESHMAN', 'Freshman'),
        ('SOPHOMORE', 'Sophomore'),
        ('JUNIOR', 'Junior'),
        ('SENIOR', 'Senior'),
        ('GRADUATE', 'Graduate'),
    ]


	title = models.CharField(max_length=255,verbose_name="Заголовок")
	content = models.TextField(blank=True,verbose_name="Настройки")
	photo = models.URLField(max_length=255,blank=True,verbose_name="Изображения")	
	time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
	time_update = models.DateTimeField(auto_now=True,verbose_name="Последнее обновление")
	is_published = models.BooleanField(default=True,verbose_name="Опубликованно")
	

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
	time_update = models. DateTimeField (auto_now=True,verbose_name="Последнее обновление")
	is_published = models. BooleanField(default=True,verbose_name="Опубликованно")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('post', kwargs={'post_id': self.pk})

	class Meta:
		verbose_name = 'Фаил'
		verbose_name_plural = 'Файлы'



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

