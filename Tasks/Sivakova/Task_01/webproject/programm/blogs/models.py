from django.db import models
from django.core.validators import int_list_validator
# Create your models here.

    

class Articles (models.Model):
    titl = models.CharField('Название услуги', max_length=250)
    shorttitle = models.CharField('Стоимость услуги', max_length=200)
    content = models.TextField('Об услуге')
    issued = models.DateTimeField('')
    image = models.ImageField(upload_to='images/', blank = True, null=True)
    
class Visitors(models.Model):
    CHOISE = [
    ('Собака','Собака'),
    ('Кот','Кот'),
    ('Грызун','Грызуны'),
    ('Птица','Птица') ]
    CHOISE_VAR = [
    ('Первичный осмотр','Первичный осмотр'),
    ('Терапия','Терапия'),
    ('Стоматология','Стоматология'),
    ('Хирургия','Хирургия'),
    ('Кастрация/стерилизация','Кастрация/стерилизация'),
    ]
    DAY_NUMBERS = [ ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'),('10','10'),('11','11'), ('12','12'), ('13','13'),
                   ('14','14'), ('15','15'), ('16','16'), ('17','17'), ('18','18'), ('19','19'), ('20','20'), ('21','21'), ('22','22'), ('23','23'), ('24','24'), ('25','25'),
                   ('26','26'), ('27','27'), ('28','28'), ('29','29'), ('30','31'),
    ]
    MONTH_NUMBERS = [ ('Января','Января'), ('Февраля','Февраля'), ('Марта','Марта'), ('Апреля','Апреля'), ('Мая','Мая'), ('Июня','Июня'), ('Июля','Июля'), ('Августа','Августа'),
                     ('Сентября','Сентября'), ('Октября','Октября'), ('Ноября','Ноября'), ('Декабря','Декабря'), 
        
    ]
 
    
    title = models.CharField('Фамилия', max_length=250)
    surname = models.CharField('Имя', max_length=200)
    option = models.CharField('Вид питомца',max_length=100, choices=CHOISE)
    optionvarone = models.CharField('Вид услуги',max_length=100, choices=CHOISE_VAR, default='Первичный осмотр')
    optionvartwo = models.CharField('Вид услуги',max_length=100, choices=CHOISE_VAR, default='Терапия')
    optionvarthree = models.CharField('Вид услуги',max_length=100, choices=CHOISE_VAR, default='Стоматология')
    optionvarfour = models.CharField('Вид услуги',max_length=100, choices=CHOISE_VAR, default='Хирургия')
    optionvarfive = models.CharField('Вид услуги',max_length=100, choices=CHOISE_VAR, default='Кастрация/стерилизация')
    content = models.TextField ('Комментарии/пожелания', blank = True, null=True)
    email = models.EmailField(blank=True, null=True)
    date = models.CharField('Дата записи',max_length=100, choices=DAY_NUMBERS, default='1')
    month = models.CharField('Месяц записи',max_length=100, choices=MONTH_NUMBERS, default='1')
    time = models.CharField('Время записи',max_length=5, unique=True, blank = False, null=True, default='00:00')
    
    
    
    
    
class Comments(models.Model):
    CHOISE_COM= [
    ('Отличное','Отличное'),
    ('Удволетворительное','Удволетворительное'),
    ('Неудволетворительное','Неудволетворительное')]
    
    name = models.CharField('Фамилия', max_length=250)
    surname = models.CharField('Имя', max_length=200)
    content = models.TextField ('Ваш отзыв', blank = False, null=True)
    choice = models.CharField('Моя оценка',max_length=100, choices=CHOISE_COM, default='Отличное')
    
    
class Doctors(models.Model):
    name = models.CharField('Имя', max_length=250)
    surname = models.CharField('Фамилия', max_length=200)
    content = models.TextField ('Специализация', blank = False, null=True)
    exp = models.CharField('Опят работы', max_length=250)
    image = models.ImageField(upload_to='images/', blank = True, null=True)
   
    def __str__(self):
        return self.name
    
    
    
  