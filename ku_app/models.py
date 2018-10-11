from django.db import models
from django.conf import settings

# Create your models here.

class Client(models.Model):
	FIO_Client = models.CharField(verbose_name = 'ФИО клиента', max_length = 100)
	INN_Client = models.CharField(verbose_name = 'ИНН клиента', max_length = 9)
	Phone_Client = models.CharField(verbose_name = 'Телефон клиента', max_length = 9)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	Time_Create = models.DateTimeField(auto_now_add=True)