from django import forms

import os
from docxtpl import DocxTemplate

class ClientForm(forms.Form):
	FIO_Client = forms.CharField(label = 'ФИО клиента', max_length = 100)
	INN_Client = forms.CharField(label = 'ИНН клиента', max_length = 9)
	Phone_Client = forms.CharField(label = 'Телефон клиента', max_length = 9)